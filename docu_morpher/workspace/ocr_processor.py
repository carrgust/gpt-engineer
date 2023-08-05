from typing import List
import pytesseract
from PIL import Image
import io

class OCRProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

    def perform_ocr(self, images: List[Tuple[int, bytes]]) -> List[str]:
        ocr_text_data = []
        for _, image_data in images:
            image = Image.open(io.BytesIO(image_data))
            ocr_text = pytesseract.image_to_string(image)
            ocr_text_data.append(ocr_text)
        return ocr_text_data
