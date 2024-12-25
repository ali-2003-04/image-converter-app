import os
from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    try:
        # Open the image using Pillow
        image = Image.open(file.stream)

        # Get the desired output format from the form (e.g., PNG, JPG)
        output_format = request.form['format'].upper()

        # Convert the image to the desired format
        img_io = io.BytesIO()
        image.save(img_io, output_format)
        img_io.seek(0)

        return send_file(img_io, mimetype=f'image/{output_format.lower()}', 
                        as_attachment=True, 
                        download_name=f'converted_image.{output_format.lower()}')

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)