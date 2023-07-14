import fitz
import os
import pytesseract
from PIL import Image
import cv2
import numpy as np

class GetTextFromPDF:
    def capture_pdf_pages(self, pdf_path):
        # Open the PDF file using PyMuPDF
        with fitz.open("pdf",pdf_path.read()) as pdf:
            text = ""
            print('*****************'+str(pdf_path)+'*******************')
            # Iterate over each page in the PDF
            for page_num in range(pdf.page_count):
                # Get the page object
                page = pdf.load_page(page_num)

                # Render the page as an image
                pix = page.get_pixmap()

                # Convert pixmap image to OpenCV format
                cv_image = self.pixmap_to_cv_image(pix)

                # Preprocess the image
                preprocessed_image = self.preprocess_image(cv_image)

                # Convert the preprocessed image to PIL format
                pil_image = Image.fromarray(preprocessed_image)

                # Perform OCR and extract text
                page_text = pytesseract.image_to_string(pil_image)
                text += page_text

        # Print the extracted text from all pages
        return text

    def pixmap_to_cv_image(self, pixmap):
        # Convert pixmap image to OpenCV format (BGR)
        width, height = pixmap.width, pixmap.height
        buffer = pixmap.samples

        # Ensure the buffer size matches the expected size
        expected_size = height * width * 3
        if len(buffer) != expected_size:
            raise ValueError("Mismatch in buffer size and expected size")

        image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 3))

        return image

    def preprocess_image(self, image):
        # Apply image enhancement techniques
        # Example: Perform image sharpening using Laplacian filter
        sharpened_image = cv2.Laplacian(image, cv2.CV_8U)

        # Other preprocessing steps (e.g., denoising, contrast adjustment) can be added here

        return sharpened_image