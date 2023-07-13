from coro import GetTextFromPDF

class Convertion:
    def wantsearch(self, pdf_path):
        text=" "
        if text.isspace():
            pdfparser=GetTextFromPDF()
            output=pdfparser.capture_pdf_pages(pdf_path=pdf_path)
            if 'internships' in output:
                return "operation successful"+output[1:100]
        return "operation failed"