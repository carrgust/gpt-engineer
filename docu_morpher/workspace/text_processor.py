from typing import List
import spacy

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text: List[str]) -> List[str]:
        processed_text_data = []
        for raw_text in text:
            doc = self.nlp(raw_text)
            processed_text = " ".join([token.text for token in doc])
            processed_text_data.append(processed_text)
        return processed_text_data
