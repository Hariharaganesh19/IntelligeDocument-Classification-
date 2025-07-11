import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import numpy as np
import easyocr
import io
from huggingface_hub import InferenceClient

st.set_page_config(page_title="📄 Document OCR & Multi-Page LLM Extraction", layout="wide")
st.title("📄 Document OCR + Unified LLM Extraction")
st.markdown("Upload a PDF or Image. This app will OCR each page and send the entire document to an LLM for unified extraction.")

reader = easyocr.Reader(['en'], gpu=False)
client = InferenceClient(
    provider="together",
    api_key="5fad45f2a2dbccebf7a6d0252ce57572471fcd28bc53e775eacbef7f43963da0"
)

uploaded_file = st.file_uploader("📁 Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

def run_ocr_on_image(img_pil):
    return reader.readtext(np.array(img_pil))

if uploaded_file:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    document_ocr_text = ""

    if file_ext == "pdf":
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            st.image(img, caption=f"Page {page_number + 1}", use_container_width=True)

            results = run_ocr_on_image(img)
            page_text = " ".join([t for _, t, _ in results])

            document_ocr_text += f"\n\nPage {page_number + 1}:\n{page_text}"

    elif file_ext in ["png", "jpg", "jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        results = run_ocr_on_image(image)
        page_text = " ".join([t for _, t, _ in results])
        document_ocr_text = f"Page 1:\n{page_text}"

    if document_ocr_text.strip():
        st.markdown("## 🧾 Full Document OCR")
        st.text_area("📜 Combined OCR Text", document_ocr_text, height=300)

        full_prompt = f"""
You are an intelligent assistant that analyzes a multi-page document.

Each page is labeled as "Page X:" and followed by its OCR text.

Your tasks:
1. Identify and classify each document type present (PAN Card, Aadhar Card, Bank Statement, Others).
2. For each document, extract the appropriate fields.
3. If a Bank Statement exists, extract **all transactions** across all related pages.

Return your response strictly in this JSON format:

{{
  "documents": [
    {{
      "document_type": "<PAN Card | Aadhar Card | Bank Statement | Others>",
      "pages": [1, 2, ...],
      "extracted_fields": {{
        ... extracted fields depending on type ...
        "Transactions": [ {{ Date, Description, Amount, Type, Balance }} ]
      }}
    }},
    ...
  ]
}}

OCR Text:
\"\"\"
{document_ocr_text}
\"\"\"
"""

        with st.spinner("🧠 Analyzing full document..."):
            completion = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=[
                    {"role": "system", "content": "You are an intelligent assistant that extracts structured data from documents."},
                    {"role": "user", "content": full_prompt}
                ],
                max_tokens=2000
            )
            response = completion.choices[0].message.content
            st.markdown("Extracted Results")
            st.code(response, language="json")
