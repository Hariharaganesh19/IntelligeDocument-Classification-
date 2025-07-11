# IntelligeDocument-Classification-
Please find the BRD for the usecase belowDocuVision: Intelligent Document Classification & Data Extraction ServiceObjective:
 To develop a web-based service that allows users to upload various types of documents (images or PDFs like bank statements, PAN, and Aadhar cards) and automatically classify the document type, extract relevant information, and present structured inference to the user.Functional Requirements

Model Performance Summary
The document classification and data extraction model demonstrates strong performance across various document types. It accurately identifies and extracts information from PAN cards and Aadhar cards, even when the images are slightly blurred or of moderate quality. However, in cases where the image quality is significantly degraded, certain key data fields may not be captured correctly.

For bank statements, the model generally performs well in extracting transaction details, including date, description, amount, type (credit/debit), and balance. Nevertheless, there are occasional inaccuracies in interpreting low-value transactions. For example, a ₹20 transaction was misread as ₹120 due to alignment issues with nearby lines. Despite this, the model maintains high accuracy in handling most typical bank statement formats.

When processing other document types, the model reliably classifies and flags them as "Others" if unsupported, ensuring robust handling of diverse input formats.

