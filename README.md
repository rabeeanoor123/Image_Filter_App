
# Image Filter App

Easily apply various filters to your images using this Streamlit app!

![Image Filter App Preview](https://imagefilterapp.streamlit.app/)

## Description

The Image Filter App is a simple tool built using Streamlit, OpenCV, and PIL. With this app, you can upload an image and apply one of several predefined filters. Once the filter is applied, you can download the modified image.

## Features

- **Multiple Filters**: Choose from a range of filters including:
    - Grayscale
    - Sepia
    - Gaussian Blur
    - Canny Edges
    - Color Inversion
    - Colorize
    - Artistic
    - Cartoon
    - Hand Sketch
- **Interactive UI**: Intuitive UI to easily upload, preview, apply filters, and download images.
- **Customizable Blur Intensity**: Adjust the intensity of the Gaussian Blur filter using a slider.

## How to Use

1. Visit the [Image Filter App](https://imagefilterapp.streamlit.app/).
2. Upload an image using the provided uploader.
3. Choose a filter from the sidebar.
4. (Optional) Adjust the blur intensity if you chose the Gaussian Blur filter.
5. Click "Apply Filter" to see the filtered image.
6. Download the filtered image by clicking the "Download Filtered Image" button.

## Code Overview

- The code uses the OpenCV library to apply various image processing techniques.
- The Streamlit library is used for the web interface, allowing for file uploads, image previews, and user interactions.
- The PIL library is used for handling image data and conversions.

## Setup and Installation

To run the app locally:

1. Install the required libraries:
    ```
    pip install streamlit opencv-python Pillow
    ```
2. Clone the repository or download the code.
3. Navigate to the code directory in your terminal.
4. Run the app using:
    ```
    streamlit run app.py
    ```

## Feedback and Contributions

Feel free to fork the repository, open issues, or submit pull requests. Any feedback is welcome!
