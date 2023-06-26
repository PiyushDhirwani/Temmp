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
        # Save the file to a desired location
        file.save(os.path.join('uploads', file.filename))
        # Process the file or folder as required
        # Here, you can read the contents of the file, or iterate through the folder contents

        return 'File uploaded successfully.'
    else:
        return 'No file uploaded.'
