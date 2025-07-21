import pytesseract
import os

# Tesseract path
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# pytesseract path
if os.name == 'nt':  # for Windows
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
