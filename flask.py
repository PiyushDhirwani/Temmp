from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/input', methods=['GET'])
def get_input():
    return '''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/input', methods=['POST'])
def post_input():
    if 'file' in request.files:
        file = request.files['file']
        file.save(os.path.join('uploads', file.filename))
        return 'File uploaded successfully.'
    else:
        return 'No file uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
