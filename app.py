from flask import Flask, request, jsonify,render_template
import os
import random

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']

    # Process the image using MobileNetV2 (placeholder for actual processing)
    result = process_image_mock()

    return jsonify({'result': result})

def process_image_mock():
    # Placeholder for actual image processing using MobileNetV2
    # For demo purposes, return random results (malignant, benign, or normal)
    results = ['Malignant', 'Benign', 'Normal']
    return random.choice(results)
current_dir = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    app.run(debug=True)
