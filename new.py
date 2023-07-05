import os
import pdfplumber
from flask import Flask, request

app = Flask(__name__)

def extract_text_from_pdf(file):
    text=""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    if file.filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file)
        # Perform further processing on the extracted text
        # For example, you can save it to a file or pass it to another function
        # Here, we simply return the extracted text as the API response
        return extracted_text

    return 'Unsupported file format', 400

if __name__ == '__main__':
    app.run()