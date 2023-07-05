from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    # Perform any necessary processing on the file
    # For example, you can save the file to a specific location
    # or process its contents

    file.save('path/to/save/file')  # Save the file to a specific location

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
