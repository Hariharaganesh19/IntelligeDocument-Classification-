# IntelligeDocument-Classification-
Please find the BRD for the usecase belowDocuVision: Intelligent Document Classification & Data Extraction ServiceObjective:
 To develop a web-based service that allows users to upload various types of documents (images or PDFs like bank statements, PAN, and Aadhar cards) and automatically classify the document type, extract relevant information, and present structured inference to the user.Functional Requirements
Document Upload

Users should be able to upload files via a web interface.
Supported file types:
Image formats: .jpg, .jpeg, .png
PDF documents: .pdf
Max file size limit: 10 MB.
Document Type Detection

The system should automatically detect and classify the document type upon upload.
Supported document types (extensible):
Aadhar Card
Bank Statement
PAN Card
Others (Unknown/Unsupported)
Detection can be based on either:

OCR (Optical Character Recognition) on content keywords
Vision based model for data extraction
File metadata and structure
Accessing GenAI models
Note: Justify why did you choose the approach and what are the challenges / problems with other approachesInference / Information Extraction
Based on the detected document type, extract key information:
a) Aadhar Card:

Name
DOB
Aadhar Number
Gender
Address
b) PAN Card:

Name
Father's Name
DOB
PAN Number
b) Bank Statement:

Bank Name
Account Number (masked/unmasked)
Statement Period
List of Transactions: Date, Description, Amount, Type (Credit/Debit), Balance

Model Performance Summary
The document classification and data extraction model demonstrates strong performance across various document types. It accurately identifies and extracts information from PAN cards and Aadhar cards, even when the images are slightly blurred or of moderate quality. However, in cases where the image quality is significantly degraded, certain key data fields may not be captured correctly.

For bank statements, the model generally performs well in extracting transaction details, including date, description, amount, type (credit/debit), and balance. Nevertheless, there are occasional inaccuracies in interpreting low-value transactions. For example, a ₹20 transaction was misread as ₹120 due to alignment issues with nearby lines. Despite this, the model maintains high accuracy in handling most typical bank statement formats.

When processing other document types, the model reliably classifies and flags them as "Others" if unsupported, ensuring robust handling of diverse input formats.

