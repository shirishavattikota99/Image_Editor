from PIL import Image
import numpy as np
import cv2
import io


# 1. Load image from Streamlit uploader
def load_image(uploaded_file):
    image = Image.open(uploaded_file)   # Open image using PIL
    image = image.convert("RGB")        # Ensure 3 channels (important)
    return np.array(image)              # Convert to NumPy array


# 2. Convert image (NumPy) to bytes (for download)
def convert_to_bytes(img):
    success, buffer = cv2.imencode('.png', img)  # Encode image as PNG
    return buffer.tobytes()                      # Convert buffer to bytes


# 3. Convert RGB to BGR (for OpenCV compatibility)
def rgb_to_bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


# 4. Convert BGR to RGB (for display in Streamlit)
def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)