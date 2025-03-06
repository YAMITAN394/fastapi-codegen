import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import device, txt_model_name

txt_tokenizer = AutoTokenizer.from_pretrained(txt_model_name)
txt_model = AutoModelForCausalLM.from_pretrained(txt_model_name, torch_dtype=torch.float16).to(device)

def generate_text(prompt: str) -> str:
    inputs = txt_tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=150).to(device)
    
    with torch.no_grad():
        output = txt_model.generate(
            inputs.input_ids,
            max_length=150,
            do_sample=True,
            top_p=0.95,
            temperature=0.7
        )
    
    response_text = txt_tokenizer.decode(output[0], skip_special_tokens=True)
    return response_text