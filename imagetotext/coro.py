import fitz
import os
import pytesseract
from PIL import Image

class GetTextFromPDF:
    def capture_pdf_pages(self, pdf_path):
        # Open the PDF file
        with fitz.open("pdf",pdf_path.read()) as pdf:
            text = ""
            # Iterate over each page in the PDF
            for page_num in range(pdf.page_count):
                # Get the page object
                page = pdf.load_page(page_num)

                # Render the page as an image
                pix = page.get_pixmap()

                # Convert pixmap image to PIL image
                pil_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                # Perform OCR and extract text
                page_text = pytesseract.image_to_string(pil_image)
                text += page_text

        print(text)
            # Print the extracted text from all pages
        return text

# Example usage
