import torch
from torch.nn import functional as F
from pytorch_pretrained_bert import GPT2Tokenizer, GPT2LMHeadModel


class Gpt2_predictor:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def predict(self, request):
        text = self.tokenizer.encode(request.form['starting_tokens'])
        encoded_text, past = torch.tensor([text]), None

        for _ in range(int(request.form['sequence_length'])):
            logits, past = self.model(encoded_text, past=past)
            encoded_text = torch.multinomial(F.softmax(logits[:, -1]), 1)
            text.append(encoded_text.item())

        return self.tokenizer.decode(text)
