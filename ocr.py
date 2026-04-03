import os
from dotenv import load_dotenv

load_dotenv()

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Strip any surrounding quotes that dotenv may include on Windows
tesseract_path = os.environ.get("TESSERACT_PATH", "").strip().strip('"').strip("'")
poppler_path = os.environ.get("POPPLER_PATH", "").strip().strip('"').strip("'")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
# If not set, tesseract must be in system PATH (Linux/Mac)


def extract_text(image_path: str) -> str:
    """Extract text from an image file using OCR."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)


def extract_text_from_pdf(pdf_path: str) -> str:
    """Convert PDF pages to images then extract text via OCR."""
    kwargs = {"pdf_path": pdf_path}
    if poppler_path:
        kwargs["poppler_path"] = poppler_path

    images = convert_from_path(**kwargs)
    full_text = ""
    for img in images:
        full_text += pytesseract.image_to_string(img) + "\n"
    return full_text
