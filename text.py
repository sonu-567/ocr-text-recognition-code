import cv2
import pytesseract
from PIL import Image

# If using Windows, set path like:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image_path = "sample.jpg"
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold (improves accuracy)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save processed image (optional)
cv2.imwrite("processed.png", thresh)

# Extract text
text = pytesseract.image_to_string(Image.open("processed.png"))

# Output
print("Extracted Text:")
print(text)
