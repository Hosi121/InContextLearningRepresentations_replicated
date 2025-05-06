import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(model_name="EleutherAI/pythia-410m"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer
