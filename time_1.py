from pdf2image import convert_from_path
from pytesseract import image_to_string

def get_text_from_any_pdf(pdf_file):
    images = convert_from_path(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += image_to_string(img)
    return final_text

print(get_text_from_any_pdf("Test.pdf"))