import PyPDF2
from docx import Document

# Open the PDF file in read-binary mode
with open('yourDocument.pdf', 'rb') as file:
    # Create a PdfReader object
    pdf = PyPDF2.PdfReader(file)
    
    # Create a new Word document
    document = Document()
    
    # Iterate over each page in the PDF
    for page_num in range(len(pdf.pages)):
        # Extract text from the page
        page = pdf.pages[page_num]
        text = page.extract_text()
        print(f"Text from page {page_num + 1}:\n{text}\n")
        
        # Add the extracted text as a paragraph to the Word document
        document.add_paragraph(text)
    
# Save the Word document
document.save('Sample1.docx')
