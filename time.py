import PyPDF2
import pytesseract
from PIL import Image

def convert_image_pdf_to_searchable_pdf(input_path, output_path):
    # Open the image PDF and extract images
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page in pdf_reader.pages:
            images = page.extract_images()
            
            # Iterate through the extracted images
            for i, image in enumerate(images):
                image_data = image['data']
                image_pil = Image.fromarray(image_data)
                
                # Perform OCR on the image using pytesseract
                ocr_text = pytesseract.image_to_pdf_or_hocr(image_pil, extension='pdf')
                
                # Create a new PDF page with the OCR text
                pdf_writer.add_page()
                pdf_writer.add_page(contents=ocr_text)
    
    # Save the searchable PDF
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Specify the paths for the input image PDF and the output searchable PDF
input_pdf_path = 'path/to/input/image.pdf'
output_pdf_path = 'path/to/output/searchable.pdf'

# Convert the image PDF to a searchable PDF
convert_image_pdf_to_searchable_pdf(input_pdf_path, output_pdf_path)






import pdfplumber
import pytesseract
from PIL import Image

def convert_image_pdf_to_searchable_pdf(input_path, output_path):
    with pdfplumber.open(input_path) as pdf:
        pdf_writer = PyPDF2.PdfWriter()
        
        for page in pdf.pages:
            images = page.images
            
            for i, image in enumerate(images):
                image_data = image['stream'].get_data()
                image_pil = Image.open(io.BytesIO(image_data))
                
                ocr_text = pytesseract.image_to_pdf_or_hocr(image_pil, extension='pdf')
                
                pdf_writer.add_page()
                pdf_writer.add_page(contents=ocr_text)
    
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Specify the paths for the input image PDF and the output searchable PDF
input_pdf_path = 'path/to/input/image.pdf'
output_pdf_path = 'path/to/output/searchable.pdf'

# Convert the image PDF to a searchable PDF
convert_image_pdf_to_searchable_pdf(input_pdf_path, output_pdf_path)









import pdfplumber
import pytesseract
from PIL import Image
from io import BytesIO

def convert_image_pdf_to_searchable_pdf(input_path, output_path):
    with pdfplumber.open(input_path) as pdf:
        pdf_writer = pdfplumber.PDF(output_path)
        
        for page in pdf.pages:
            images = page.images
            
            for i, image in enumerate(images):
                image_data = image["stream"].get_rawdata()
                image_pil = Image.open(BytesIO(image_data))
                
                # Perform OCR on the image using pytesseract
                ocr_text = pytesseract.image_to_pdf_or_hocr(image_pil, extension='pdf')
                
                # Add the OCR text as a new page to the PDF writer
                pdf_writer.add_page(ocr_text)
    
    # Save the searchable PDF
    pdf_writer.save()

# Specify the paths for the input image PDF and the output searchable PDF
input_pdf_path = 'path/to/input/image.pdf'
output_pdf_path = 'path/to/output/searchable.pdf'

# Convert the image PDF to a searchable PDF
convert_image_pdf_to_searchable_pdf(input_pdf_path, output_pdf_path)
