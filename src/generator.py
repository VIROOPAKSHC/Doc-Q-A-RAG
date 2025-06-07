
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

model_name = "TheBloke/LLaMA-2-7B-GPTQ"  # or your model

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16"
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config,
    trust_remote_code=True  # required for some GPTQ models
)

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

def generate_answer(context, question):
    prompt = f"""[CONTEXT]\n{context}\n\n[QUESTION]\n{question}\n\n[ANSWER]\n"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=256)
    return tokenizer.decode(output[0], skip_special_tokens=True)
