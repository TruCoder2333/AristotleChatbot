import re
import os
from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def clean_text(text: str) -> str:

    text = text.strip()
    
    text = re.sub(r'\s+', ' ', text)
    
    text = re.sub(r'[^\x20-\x7E\u0400-\u04FF]+', '', text)
    
    text = text.lower()
    
    return text

if __name__=="__main__":
    for filename in os.listdir(RAW_DATA_DIR):

        input_path = os.path.join(RAW_DATA_DIR, filename)
        output_path = os.path.join(PROCESSED_DATA_DIR, f"clean_{filename}.txt")
        print(input_path)
        print(output_path)
        with open(input_path, "r", encoding="utf-8") as raw_text_file:
            raw_text = raw_text_file.read()
            processed_text = clean_text(raw_text)
        
        with open(output_path, "w", encoding="utf-8") as processed_file:
            processed_file.write(processed_text)