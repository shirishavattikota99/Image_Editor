import streamlit as st
from filters import *
from utils import *

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Image Editor",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Editor with OpenCV")

# ---------------- STORE IMAGE ---------------- #
uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png", "webp"]
)

# Save uploaded image in session_state
if uploaded_file:
    st.session_state.image = uploaded_file

# ---------------- RESET BUTTON ---------------- #
if st.sidebar.button("Reset Filters"):
    st.session_state.blur = 1
    st.session_state.brightness = 0
    st.session_state.contrast = 1.0
    st.session_state.sharpness = 0.0
    st.session_state.t1 = 100
    st.session_state.t2 = 200
    st.session_state.edge = False
    st.session_state.gray = False
    st.rerun()

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Filters")

# Sliders with keys
blur = st.sidebar.slider("Blur", 1, 51, 1, key="blur")
brightness = st.sidebar.slider("Brightness", -100, 100, 0, key="brightness")
contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0, key="contrast")
sharpness = st.sidebar.slider("Sharpness", 0.0, 3.0, 0.0, key="sharpness")

# Edge thresholds
t1 = st.sidebar.slider("Edge Threshold 1", 0, 255, 100, key="t1")
t2 = st.sidebar.slider("Edge Threshold 2", 0, 255, 200, key="t2")

# Toggles
edge = st.sidebar.checkbox("Edge Detection", key="edge")
gray = st.sidebar.checkbox("Grayscale", key="gray")

# ---------------- MAIN LOGIC ---------------- #
if "image" in st.session_state:
    uploaded_file = st.session_state.image

    # Load image
    img = load_image(uploaded_file)

    # Convert to BGR
    img_bgr = rgb_to_bgr(img)

    # Copy image
    processed = img_bgr.copy()

    # APPLY FILTERS (STACKED)
    processed = Blur(processed, blur)
    processed = Brightness(processed, brightness)
    processed = Contrast(processed, contrast)
    processed = Sharpen(processed, sharpness)

    if gray:
        processed = Grayscale(processed)

    if edge:
        processed = Edge_Detection(processed, t1, t2)

    # Convert back for display
    processed_display = bgr_to_rgb(processed) if not gray and not edge else processed

    # DISPLAY
    col1, col2 = st.columns(2)

    with col1:
        st.image(img, caption="Original Image", use_container_width=True)

    with col2:
        st.image(processed_display, caption="Processed Image", use_container_width=True)

    # DOWNLOAD
    st.download_button(
        label="⬇️ Download Image",
        data=convert_to_bytes(processed),
        file_name="edited_image.png",
        mime="image/png"
    )