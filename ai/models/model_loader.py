import os
import torch
from transformers import AutoModel, AutoTokenizer

class ModelLoader:
    def __init__(self, model_name='ggml-alpaca-7b-q4', model_path='./ggml_alpaca_7b_q4.bin'):
        self.model_name = model_name
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        try:
            self.model = AutoModel.from_pretrained(self.model_path)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        except Exception as e:
            raise ValueError(f"Failed to load the model: {str(e)}")

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.logits

    def transform(self, data):
        transformed_data = []
        for item in data:
            transformed_item = self.preprocess(item)
            transformed_data.append(transformed_item)
        return transformed_data

    def preprocess(self, text):
        return self.tokenizer(text, padding=True, truncation=True, return_tensors='pt')

    def postprocess(self, logits):
        probabilities = torch.softmax(logits, dim=-1)
        return probabilities.argmax(-1)
