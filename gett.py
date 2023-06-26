from flask import Flask, request
import os
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/input', methods=['GET'])
def get_input():
    return '''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" multiple webkitdirectory directory>
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/input', methods=['POST'])
def post_input():
    if 'file' in request.files:
        files = request.files.getlist('file')

        # Create the uploads folder if it doesn't exist
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        for file in files:
            if file.filename:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return 'Files uploaded successfully.'
    else:
        return 'No files uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
