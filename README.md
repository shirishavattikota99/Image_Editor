# Image Editor with Streamlit & OpenCV

## 📌 Project Description

This project is a browser-based Image Editing Application built using Python.
It allows users to upload an image, apply multiple image processing filters, preview the results in real time, and download the edited image.

The application uses:

* **Streamlit** for the user interface
* **OpenCV** for image processing
* **NumPy** for image array manipulation

---

##  Features

*  Upload images (JPG, JPEG, PNG)
*  Apply multiple filters using sliders and checkboxes
*  Real-time preview of changes
*  Filters are stackable (applied sequentially)
*  Download edited image as PNG

---

##  Filters Implemented

1. **Blur** – Smooths the image using Gaussian Blur
2. **Brightness** – Adjusts image intensity
3. **Contrast** – Enhances or reduces contrast
4. **Sharpness** – Highlights edges
5. **Edge Detection** – Detects edges using Canny algorithm
6. **Grayscale** – Converts image to grayscale

---

##  Technologies Used

* Python
* Streamlit
* OpenCV
* NumPy
* Pillow

---

## 📁 Project Structure

```
image_editor/
│
├── app.py              # Main Streamlit app
├── filters.py          # Image processing functions
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

Installation & Setup
Step 1: Clone the Repository

git clone https://github.com/your-username/image-editor.git
cd image-editor

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Application
streamlit run app.py
