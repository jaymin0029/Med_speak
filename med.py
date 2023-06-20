import os
import requests

os.environ['tika-app-2.8.0.jar'] = '"file:////tika_files/tika-app-2.8.0.jar'

import tika
tika.initVM()
from tika import parser

def chat_with_chatgpt(content):
    res = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR KEY" 
        },
        json={
            "messages": [{"role": "user", "content": content}, ] ,
            "max_tokens": 200,
            "model": "gpt-3.5-turbo"
        }
    )
    return res

def extract_text(filepath):
    parsed = parser.from_file(filepath)
    content = parsed["content"]

    return content
