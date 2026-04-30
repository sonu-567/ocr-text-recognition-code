# 🧠 Text Recognition using OCR (Python)

## 📌 Project Overview

This project implements a simple **Optical Character Recognition (OCR)** system using Python.
It extracts text from images using the Tesseract OCR engine.

---

## 🎯 Objective

* To read and extract text from an image
* To preprocess images for better accuracy
* To understand basic computer vision and OCR concepts

---

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* pytesseract
* Pillow (PIL)

---

## 📂 Project Structure

```
project/
│── sales.py
│── sample.jpg
│── processed.png (generated)
│── README.md
```

---

## ⚙️ Installation

### 1. Install Python Libraries

```bash
pip install opencv-python pytesseract pillow
```

### 2. Install Tesseract OCR

#### 🔹 Windows:

* Download and install Tesseract from:
  https://github.com/tesseract-ocr/tesseract

* Set path in code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### 🔹 Linux:

```bash
sudo apt install tesseract-ocr
```

---

## ▶️ How to Run

1. Place your image in the project folder
2. Rename it as `sample.jpg` (or update path in code)
3. Run the script:

```bash
python sales.py
```

---

## 🔄 Working Process

1. **Input Image** → Load using OpenCV
2. **Preprocessing**

   * Convert to grayscale
   * Apply thresholding
3. **Text Extraction**

   * Use pytesseract to read text
4. **Output**

   * Display extracted text in console

---

## 🧪 Sample Code

```python
import cv2
import pytesseract
from PIL import Image

image_path = "sample.jpg"
img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite("processed.png", thresh)

text = pytesseract.image_to_string(Image.open("processed.png"))

print("Extracted Text:")
print(text)
```

---

## 📊 Output Example

```
Extracted Text:
Hello Sonu Shivam
Artificial Intelligence Project
```

---

## 🚀 Features

* Simple and easy to use
* Works with printed text images
* Improves accuracy using preprocessing

---

## ⚠️ Limitations

* Less accurate for handwritten text
* Requires good image quality
* Needs proper lighting and contrast

---

## 🔮 Future Improvements

* Add GUI interface
* Support for multiple languages
* Real-time text detection using camera
* Improve preprocessing using filters

---

## 👨‍💻 Author

**Sonu Shivam**

---

## 📜 License

This project is for educational purposes.
