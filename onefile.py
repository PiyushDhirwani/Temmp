import pdfplumber


class Extracttestfrom:
    @staticmethod
    def extract_text_from_pdf(file):
        text=""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text