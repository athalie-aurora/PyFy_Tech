from flask import Flask, render_template, request, url_for
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np
import pytesseract
from PIL import Image
import uuid  
import cv2
import datetime
import requests

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Load pre-trained model
model = VGG16(weights='imagenet')

# Tentukan folder untuk menyimpan file yang diunggah
UPLOAD_FOLDER = 'static/images'
TEXT_FOLDER = 'static/texts'
VIDEO_FOLDER = 'static/videos'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEXT_FOLDER'] = TEXT_FOLDER
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER

# Memastikan folder upload, text, dan video ada
for folder in [UPLOAD_FOLDER, TEXT_FOLDER, VIDEO_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

@app.route('/hello', methods=['GET'])
def hello_world():
    return render_template('hello_home.html')

@app.route('/features', methods=['GET'])
def features():
    return render_template('features.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_image():
    image_path = None 
    prediction = None  
    if request.method == 'POST':
        imagefile = request.files['imagefile']
        if imagefile:
            filename = imagefile.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagefile.save(image_path)

            # Lakukan prediksi gambar
            image = load_img(image_path, target_size=(224, 224))
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = preprocess_input(image)

            yhat = model.predict(image)
            label = decode_predictions(yhat, top=1)[0][0]
            prediction = f"{label[1]} ({label[2]*100:.2f}%)"
            
            image_path = url_for('static', filename='images/' + filename) 

    return render_template('imagepredict.html', image_path=image_path, prediction=prediction)

@app.route('/extract', methods=['GET', 'POST'])
def extract_text():
    image_path = None 
    extracted_text = None 
    text_file_url = None  
    if request.method == 'POST':
        imagefile = request.files.get('image')  # Pastikan untuk menggunakan .get('image') untuk menghindari KeyError
        if imagefile:
            filename = imagefile.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagefile.save(image_path)
    
            # Ekstraksi teks dari gambar menggunakan pytesseract
            extracted_text = pytesseract.image_to_string(Image.open(image_path))
            
            # Simpan teks yang diekstraksi ke file .txt
            text_filename = f"{uuid.uuid4()}.txt"
            text_file_path = os.path.join(app.config['TEXT_FOLDER'], text_filename)
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(extracted_text)
            
            image_path = url_for('static', filename='images/' + filename)
            text_file_url = url_for('static', filename='texts/' + text_filename)
            
    return render_template('imageextract.html', image_path=image_path, extracted_text=extracted_text, text_file_url=text_file_url)

@app.route('/detect', methods=['GET', 'POST'])
def detect_video():
    if request.method == 'POST':
        if 'video' not in request.files:
            return jsonify({'error': 'No video part'}), 400
        video = request.files['video']
        if video.filename == '':
            return jsonify({'error': 'No selected video'}), 400
        
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
        video_path = os.path.join(app.config['VIDEO_FOLDER'], filename)
        video.save(video_path)

        return jsonify({'video_path': url_for('static', filename='videos/' + filename)})
    else:
        return render_template('detect.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
