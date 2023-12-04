from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from processing import *

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Replace the following line with your actual image processing code
        result = predict_prostate_cancer(filepath)

        return jsonify({'result': result})

    return jsonify({'error': 'Invalid file format'})

def predict_prostate_cancer(img_path):
    try:
        # Your image processing code here
        result = 'Positive'  # Replace with actual processing code
        return result
    except Exception as e:
        print("Error during image processing:", str(e))
        return 'Error'

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
