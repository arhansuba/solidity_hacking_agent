# transformers/model.py

from transformers import BertTokenizer, BertForSequenceClassification
import torch

class TransformersModel:
    def __init__(self, model_name: str = 'bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)

    def predict(self, text: str) -> torch.Tensor:
        inputs = self.tokenizer(text, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.logits

    def save_model(self, path: str):
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def load_model(self, path: str):
        self.model = BertForSequenceClassification.from_pretrained(path)
        self.tokenizer = BertTokenizer.from_pretrained(path)

# Example usage
if __name__ == "__main__":
    model = TransformersModel()
    text = "The new model performs exceptionally well."
    logits = model.predict(text)
    print(f"Logits: {logits}")
