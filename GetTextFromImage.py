from pdf2image import convert_from_path
from pytesseract import image_to_string


class GetTextFromPdf:
    def gettextimage(self, filename):
        images = convert_from_path(filename)
        final_text = ""
        for pg, img in enumerate(images):
            
            final_text += image_to_string(img)
        return final_text
