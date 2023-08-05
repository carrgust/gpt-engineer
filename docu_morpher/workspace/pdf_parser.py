import fitz  # PyMuPDF
from typing import List, Tuple

class PDFParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.doc = fitz.open(file_path)

    def extract_text(self) -> List[str]:
        text_data = []
        for page in self.doc:
            text_data.append(page.get_text("text"))
        return text_data

    def extract_images(self) -> List[Tuple[int, bytes]]:
        images_data = []
        for page in self.doc:
            image_list = page.get_images(full=True)
            for img in image_list:
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                images_data.append((xref, base_image["image"]))
        return images_data

    def extract_layout(self) -> List[Tuple[float, float, float, float]]:
        layout_data = []
        for page in self.doc:
            blocks = page.get_text("blocks")
            for block in blocks:
                layout_data.append(block[:4])
        return layout_data
