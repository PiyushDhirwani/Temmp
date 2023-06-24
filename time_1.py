# from pdf2image import convert_from_path
# from pytesseract import image_to_string

# def get_text_from_any_pdf(pdf_file):
#     images = convert_from_path(pdf_file)
#     final_text = ""
#     for pg, img in enumerate(images):
#         final_text += image_to_string(img)
#     return final_text

# print(get_text_from_any_pdf("Test.pdf"))

import PyPDF2
import os

def convert_scanned_pdf(input_pdf, output_pdf):
    """Converts a scanned PDF to a text PDF.

    Args:
        input_pdf (str): The path to the input PDF file.
        output_pdf (str): The path to the output PDF file.

    Returns:
        None.
    """

    pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page).extractText()
        pdf_writer.addPage(PyPDF2.pdf.PageObject.createTextPage(text))

    pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf = "Test.pdf"
    output_pdf = "output.pdf"

    convert_scanned_pdf(input_pdf, output_pdf)

    print("Successfully converted scanned PDF to text PDF.")
