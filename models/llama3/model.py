# llama3/model.py

import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

class LLaMA3Model:
    def __init__(self, model_name: str = 'meta/llama-3'):
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name)
        self.model = LlamaForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt: str, max_length: int = 50) -> str:
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs['input_ids'], max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def save_model(self, path: str):
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def load_model(self, path: str):
        self.model = LlamaForCausalLM.from_pretrained(path)
        self.tokenizer = LlamaTokenizer.from_pretrained(path)

# Example usage
if __name__ == "__main__":
    model = LLaMA3Model()
    prompt = "The future of AI is"
    generated_text = model.generate_text(prompt)
    print(f"Generated Text: {generated_text}")
