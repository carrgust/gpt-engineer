from typing import List, Tuple
from docx import Document
from docx.shared import Inches

class WordGenerator:
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.doc = Document()

    def create_word_document(self, text_data: List[str], layout_data: List[Tuple[int, int]]) -> None:
        for text, layout in zip(text_data, layout_data):
            width, height = layout
            paragraph = self.doc.add_paragraph(text)
            paragraph_format = paragraph.paragraph_format
            paragraph_format.space_before = Inches(height / 72)
            paragraph_format.space_after = Inches(height / 72)
            paragraph_format.left_indent = Inches(width / 72)
        self.doc.save(self.output_file)
