from PIL import Image
import pytesseract
import io
from app import config  

def extract_text_from_image(image_bytes: bytes, lang: str = "fra") -> str:
    """
    Extract a text from an image using OCR (Tesseract).
    :param image_bytes: binary data of the image
    :param lang: OCR language ('fra' for français, 'eng' for english, etc.)
    :return: Extracted text
    """
    try:
        # open image
        image = Image.open(io.BytesIO(image_bytes))

        # start OCR
        text = pytesseract.image_to_string(image, lang=lang)

        return text.strip()
    except Exception as e:
        print(f"Error OCR : {e}")
        return "Error during image analysis."
