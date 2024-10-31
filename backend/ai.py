from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load the GPT-2 model and tokenizer
model_name = "gpt2"  # 'gpt2-medium', 'gpt2-large', and 'gpt2-xl' are also available for more power
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_text(prompt, max_length=200):
    # Encode the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate text with the model
    outputs = model.generate(
        inputs.input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,  # Avoid repeating phrases
        top_k=50,                # Limits sampling pool to the top 50 words
        top_p=0.95,              # Focus on words with cumulative probability of 95%
        temperature=0.7,         # Controls randomness in generation
        do_sample=True           # Sample text randomly
    )
    
    # Decode and return the generated text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example prompt
prompt = "Come up with some questions about: Netflix Joins The Handful Of Tech Companies Reporting Layoffs In The Past Week"
generated_text = generate_text(prompt)
print(generated_text)
