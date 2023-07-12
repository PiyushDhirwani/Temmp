from coro import GetTextFromPDF

class Convertion:
    def wantsearch(self, pdf_path):
        pdfparser=GetTextFromPDF()
        output=pdfparser.capture_pdf_pages(pdf_path=pdf_path)
        if 'internships' in output:
            return "operation successful"
        return "operation failed"