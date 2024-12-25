
# Image Converter App

A web-based application for converting image formats built using Flask and Pillow.

## Features
- Drag and drop image upload.
- Supports multiple output formats (PNG, JPG, GIF, BMP).
- Responsive and user-friendly design.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-converter.git
   cd image-converter
   ```
2. Install dependencies:
   ```bash
   pip install flask pillow
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`. Or use `http://192.168.1.112:5000` on another device connected to the same local network to access the Flask app by connecting to your computer’s local IP address.

## Usage
1. Upload an image by dragging and dropping it into the designated area or using the file picker.
2. Select the desired output format (PNG, JPG, GIF, BMP).
3. Click the **Convert Images** button.
4. Download the converted image when the process is complete.

## Project Structure
```
image-converter/
├── app.py             # Main Flask application
├── templates/
│   └── index.html     # HTML template for the interface
├── static/
│   └── style.css      # Styling for the application
└── README.md          # Project documentation
```
