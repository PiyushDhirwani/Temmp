from pdf2image import convert_from_path
from pytesseract import image_to_string
from fpdf import FPDF

def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image
    
    @params:
        - pdf_file: the file to be converted
    
    @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    """
    @desc: this function extracts text from image
    
    @params:
        - file: the image file to extract the content
    
    @returns:
        - the textual content of single image
    """
    
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    """
    @desc: this function is our final system combining the previous functions
    
    @params:
        - file: the original PDF File
    
    @returns:
        - the textual content of ALL the pages
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        
        final_text = convert_image_to_text(img)
        final_text = final_text.replace('\u2018', "'").replace('\u2019', "'").replace('\u2014', '-')
        for i in final_text.split('\n'):
            pdf.cell(200, 10, txt=i, ln=1,align='L')
        
        # pdf.cell(200, 10, txt=final_text, ln=1, align='C')

        #print("Page n°{}".format(pg))
        #print(convert_image_to_text(img))
    pdf.output("GFG.pdf")
    return final_text

path_to_pdf = 'Testing.pdf'

print(get_text_from_any_pdf(path_to_pdf))



# Python program to create
# a pdf file




# Replace the right 