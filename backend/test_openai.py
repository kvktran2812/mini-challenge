from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model
model_name = "valhalla/t5-base-qg-hl"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.resize_token_embeddings(len(tokenizer))


# Context for generating questions
context = "Physics, Math, Max Planck"

# Encode input for question generation
input_text = f"generate questions: {context}"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate questions
outputs = model.generate(input_ids, max_length=80, num_return_sequences=5, num_beams=5)
questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

print("------------------------------------------")
print("Here are some questions generated:")
print()
print("Generated Questions:")

for question in questions:
    print(question)
