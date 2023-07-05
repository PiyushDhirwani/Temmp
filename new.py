import os
from flask import Flask, request

app = Flask(__name__)

def process_file_or_folder(file_or_folder):
    # Perform processing on the file or folder
    # You can pass it to your desired function here
    # For demonstration purposes, let's print the input
    print("Processing:", file_or_folder)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files and 'folder' not in request.form:
        return 'No file or folder parameter in the request', 400

    file = request.files.get('file')
    folder = request.form.get('folder')

    if file:
        process_file_or_folder(file)
        return 'File processed successfully'

    if folder:
        process_file_or_folder(folder)
        return 'Folder processed successfully'

if __name__ == '__main__':
    app.run()
