from pdf_parser import PDFParser
from ocr_processor import OCRProcessor
from image_recognizer import ImageRecognizer
from text_processor import TextProcessor
from layout_analyzer import LayoutAnalyzer
from word_generator import WordGenerator

def main():
    pdf_path = "input.pdf"
    output_docx = "output.docx"
    output_ppt = "output.pptx"

    pdf_parser = PDFParser(pdf_path)
    text_data = pdf_parser.extract_text()
    images_data = pdf_parser.extract_images()
    layout_data = pdf_parser.extract_layout()

    ocr_processor = OCRProcessor()
    ocr_text_data = ocr_processor.perform_ocr(images_data)

    text_processor = TextProcessor()
    processed_text_data = text_processor.process_text(text_data + ocr_text_data)

    layout_analyzer = LayoutAnalyzer(layout_data)
    analyzed_layout_data = layout_analyzer.analyze_layout()

    word_generator = WordGenerator(output_docx)
    word_generator.create_word_document(processed_text_data, analyzed_layout_data)

    ppt_generator = WordGenerator(output_ppt)
    ppt_generator.create_word_document(processed_text_data, analyzed_layout_data)

if __name__ == "__main__":
    main()
