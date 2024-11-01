from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model
model_name = "mrm8488/t5-base-finetuned-question-generation-ap"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.resize_token_embeddings(len(tokenizer))


# Context for generating questions
context = "OWC Envoy Ultra SSD and OWC Thunderbolt 5 (USB-C) Cables Empower Mac Users Like No Other, Enabling Unmatched Speed, Reliability, and Connectivity"

# Encode input for question generation
# input_text = f"generate question to know who would interested in: {context}"
input_text = f"Ask a question to know why you would interested in: {context}"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate questions
outputs = model.generate(input_ids, max_length=80)
questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

print("------------------------------------------")
print("Here are some questions generated:")
print()
print("Generated Questions:")

for question in questions:
    print(question)
