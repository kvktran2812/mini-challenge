from transformers import T5ForConditionalGeneration, T5Tokenizer

# Corrected model name
model_name = "t5-large"  # or "google/flan-t5-large" if using FLAN-T5
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Fixed input text with closed quote
text = "What is life?"
input_text = f"Provide four unique answers to the question: '{text}'"
inputs = tokenizer.encode(input_text, return_tensors="pt")

# Adjusted generation parameters for more diverse outputs
output = model.generate(
    inputs,
    max_length=80,
    num_return_sequences=4,  # Requesting four unique answers
    temperature=0.9,         # Higher temperature for varied outputs
    top_k=50,                # Limiting to top 50 choices for coherence
    top_p=0.85               # Top-p sampling for diversity
)

# Iterating and printing answers with improved variable naming
for i, answer in enumerate(output):
    print(f"Answer {i+1}: {tokenizer.decode(answer, skip_special_tokens=True)}")
