import pdfplumber
# import os
# import pdf2image import convert_from_path
# import pytesseract
# import PyPDF2
# import time
# import pandas as pd
# from thefuzz import fuzz
# from jproperties import Properties

# configs=Properties()

# with open('application.properties', 'rb') as read_prop:
#     configs.load(read_prop)

# df=pd.read_csv("location")
# df=df.dropna()

# make=df['Legal Fund Name'].str.lower.tolist()

# pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# class PdfParser:
#     def __init__(self):
#         pass

#     def PdfLength(self, pdf_file):
#         file = open(pdf_file, 'rb')
#         readpdf = PyPDF2.PdfReader(file)
#         return len(readpdf.pages)
    
#     def GetTextFromAnyPdf(self, pdf_file):
#         images=convert_from_path(pdf_file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
#         final_text=""
#         i=0
#         for pg, img in enumerate(images):
#             i+=1
#             final_text+=pytesseract.image_to_string(img)
#             if i==3:
#                 break
#         return final_text
    
#     def PdfCheckIn(self, pdf_file):
#         possibletransfertype=["t","r","s"]
#         occ={}
#         with pdfplumber.open(pdf_file) as pdf:
#             for i in range(0,3):
#                 page=pdf.pages[i]
#                 text=page.extract_text()
#                 for line in text.split('\n'):
#                     if "occ" in line.lower():
#                         occ[i]=line.lower()


df=pd.read_csv("location.csv")
df=df.dropna()
make=df['Legal Fund Name'].str.lower().tolist()

def getFundType(self, FileName):
    text=""
    with pdfplumber.open(FileName) as pdf:
        for page in pdf.pages:
            text+=(page.extract_text().lower()+" ")

    if text.isspace():
        text=self.GetTextFromAnyPdf(FileName)
        text=text.lower()

    final=''
    curr_fuzz=-1
    for i in text.split('\n'):
        if "fund" in i:
            for fund_name in make:
                if fuzz.partial_ratio(i,fund_name)>curr_fuzz:
                    curr_fuzz=fuzz.partial_ratio(i,fund_name)
                    final=fund_name
                    if curr_fuzz==100:
                        break
    return final