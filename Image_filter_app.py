import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def dodgeV2(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)

def apply_filter(image, filter_name, blur_intensity=None):
    if filter_name == "grayscale":
        result = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif filter_name == "sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(image, kernel)

    elif filter_name == "gaussian_blur":
        return cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)

    elif filter_name == "canny_edges":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    elif filter_name == "color_inversion":
        return cv2.bitwise_not(image)

    elif filter_name == "colorize":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        norm_gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        return cv2.applyColorMap(norm_gray, cv2.COLORMAP_JET)

    elif filter_name == "artistic":
        return cv2.bilateralFilter(image, 9, 75, 75)

    elif filter_name == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon

    elif filter_name == "hand_sketch":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        inv_gray = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inv_gray, (13, 13), 0)
        sketched = dodgeV2(gray, blurred)
        return cv2.cvtColor(sketched, cv2.COLOR_GRAY2RGB)

    else:
        return image

st.title("Image Filter App")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    filter_options = ["grayscale", "sepia", "gaussian_blur", "canny_edges", "color_inversion", 
                      "colorize", "artistic", "cartoon", "hand_sketch"]

    filter_option = st.sidebar.selectbox("Choose a filter:", filter_options)

    blur_intensity = None
    if filter_option == "gaussian_blur":
        blur_intensity = st.sidebar.slider("Blur Intensity", 1, 50, 15, step=2)

    if st.sidebar.button("Apply Filter"):
        img_array = np.array(image)
        filtered_img = apply_filter(img_array, filter_option, blur_intensity)
        st.image(filtered_img, caption=f"{filter_option} Filter Applied", use_column_width=True)

        filtered_pil_image = Image.fromarray(cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB))
        buffered = io.BytesIO()
        filtered_pil_image.save(buffered, format="PNG")

        st.download_button(
            label="Download Filtered Image",
            data=buffered.getvalue(),
            file_name=f"{filter_option}_filtered.png",
            mime="image/png"
        )
