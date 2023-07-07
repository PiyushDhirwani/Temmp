import os
from flask import Flask, request
from onefile import Extracttestfrom
print("hello")
app = Flask(__name__)

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    print(request.files)
    print(request.files['file'])
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']
    
    if file.filename.endswith('.pdf'):
        extractor = Extracttestfrom()
        extracted_text = extractor.extract_text_from_pdf(file)
        # Perform further processing on the extracted text
        # For example, you can save it to a file or pass it to another function
        # Here, we simply return the extracted text as the API response
        return extracted_text

    return 'Unsupported file format', 400

if __name__ == '__main__':
    app.run()