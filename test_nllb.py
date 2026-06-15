from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)

MODEL_PATH = r"D:\AI_LANGUAGE_SUITE\final_nllb_200k"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True,
)

print("Tokenizer loaded!")

print("Loading model...")

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True,
)

print("Model loaded!")

print(type(tokenizer))
print(type(model))

print("SUCCESS")