from flask import Flask, jsonify, request
from flask import *
from GetTextFromImage import GetTextFromPdf

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/upload', methods=['POST'])
def upload_file():

    pdfparser=GetTextFromPdf()


    if 'file' not in request.files:
        return 'No file part in the request', 400
    
    file=request.files['file']

    output=pdfparser.gettextimage(file)
    return str(output)

if __name__ == '__main__':
    app.run(debug=True)