import re
from transformers import T5ForConditionalGeneration, AutoTokenizer
import nltk
nltk.download('punkt')

sample_log = """
2025-07-01 10:01:23 INFO Starting application
2025-07-01 10:01:24 DEBUG Connecting to database...
2025-07-01 10:01:25 ERROR Failed to connect to database
2025-07-01 10:01:26 INFO Retrying connection
2025-07-01 10:01:30 ERROR Connection timeout
"""
print(" Raw sample_log content:\n", sample_log)

def extract_errors(log_text):
    lines = log_text.strip().split("\n")
    error_lines = [line for line in lines if "ERROR" in line]
    return "\n".join(error_lines)

def summarize_errors(errors_text):
    if not errors_text.strip():
        return " No error lines to summarise."

    model_name = "t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    input_text = f"summarize: {errors_text}"
    print("\nInput to model:\n", f"summarize: {error_log}")


    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=50,
        min_length=10,
        num_beams=4,
        early_stopping=True)
    return tokenizer.decode(summary_ids[0],skip_special_tokens=True)


error_log = extract_errors(sample_log)
print("Errors Found:\n",error_log)


summary_log = summarize_errors(error_log)
print("\nGenerated Summary:\n", summary_log)










    

    
