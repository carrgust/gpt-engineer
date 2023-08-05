from typing import List
import requests
from google.cloud import vision

api_key="AIzaSyBoR2zZKNLIG5fDsfa0MxMOAjUvdI3Zt7o"

class ImageRecognizer:
    def __init__(self, api_key: str):
        self.client = vision.ImageAnnotatorClient()
    
    def recognize_elements(self, images: List[bytes]) -> List[List[str]]:
        labels_for_all_images = []
        for image_data in images:
            image = vision.Image(content=image_data)
            response = self.client.label_detection(image=image)
            labels = response.label_annotations
            labels_for_image = [label.description for label in labels]
            labels_for_all_images.append(labels_for_image)
        return labels_for_all_images
