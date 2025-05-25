import yaml
import requests
import time
import os
import re
from typing import Dict, Any

def is_chinese_char(char: str) -> bool:
    """Check if a character is Chinese."""
    return '\u4e00' <= char <= '\u9fff'

def get_chinese_ratio(text: str) -> float:
    """Calculate the ratio of Chinese characters in the text."""
    if not text:
        return 0.0
    chinese_chars = sum(1 for char in text if is_chinese_char(char))
    return chinese_chars / len(text)

def translate_with_ollama(text: str, model: str = "llama2", api_key: str = None, retry_count: int = 0) -> str:
    """Translate text using Ollama API with OpenAI-compatible format."""
    url = "https://models.dev.ai-links.com/v1/chat/completions"
    
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    messages = [
        # {
        #     "role": "system",
        #     "content": "You are a professional translator. Your task is to translate English text to Chinese. Only return the Chinese translation without any explanations or additional text."
        # },
        {
            "role": "user",
            "content": f'翻译成中文：\n{text}'
        }
    ]
    
    data = {
        "model": model,
        "messages": messages,
        "top_p": 0.95,
        "temperature": 0.8,  # Lower temperature for more consistent translations
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        message = response.json()["choices"][0]["message"]["content"].strip()
        print(f'eng:{text}\nzh:{message}')
        
        # Compare original and translated text
        if text.strip() == message.strip():
            print("WARNING: Original text and translation are identical! This might indicate a translation issue.")
            return message
            
        # Check Chinese character ratio for longer texts
        if len(text) > 30:
            chinese_ratio = get_chinese_ratio(message)
            print(f"Chinese character ratio: {chinese_ratio:.2%}")
            
            # If ratio is too low and we haven't retried too many times, try again
            if chinese_ratio < 0.4 and retry_count < 1:
                print(f"Low Chinese character ratio detected. Retrying translation (attempt {retry_count + 2})...")
                time.sleep(1)  # Add a small delay before retry
                return translate_with_ollama(text, model, api_key, retry_count + 1)
        
        return message
    except Exception as e:
        print(f"Error translating text: {e}")
        return ""

def process_yaml_file(input_file: str, output_file: str, api_key: str = None):
    """Process YAML file and add Chinese translations."""
    # Read the YAML file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    total_models = len(data)
    print(f"\nTotal number of models to process: {total_models}")
    
    # Process each model entry
    for idx, model in enumerate(data, 1):
        if 'description' in model:
            print(f"\nProcessing model {idx}/{total_models}: {model['name']}...")
            # Translate the description
            translation = translate_with_ollama(model['description'],'qwen2.5', api_key=api_key)
            # Add the translation to the model entry
            model['description_zh_CN'] = translation
            # Add a small delay to avoid overwhelming the API
            time.sleep(1)
    
    # Write the updated YAML to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    input_file = "gpustack/assets/model-catalog-modelscope.yaml"
    output_file = "gpustack/assets/model-catalog-modelscope-zh.yaml"
    
    # Get API key from environment variable or user input
    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        api_key = input("Please enter your Ollama API key: ")
    
    print("Starting translation process...")
    process_yaml_file(input_file, output_file, api_key)
    print("Translation completed. Output written to:", output_file) 