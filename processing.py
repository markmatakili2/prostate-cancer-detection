import os
import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

# Load a pre-trained CNN model for image classification
model = keras.applications.MobileNetV2(weights='imagenet', include_top=True)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict_prostate_cancer(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    decoded_predictions = keras.applications.mobilenet_v2.decode_predictions(predictions.numpy())[0]
    return decoded_predictions

if __name__ == "__main__":
    # Example usage
    image_path = "path/to/your/image.jpg"
    predictions = predict_prostate_cancer(image_path)

    print("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(predictions):
        print(f"{i + 1}: {label} ({score:.2f})")
