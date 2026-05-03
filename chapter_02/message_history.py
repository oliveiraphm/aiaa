import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

client = OpenAI(api_key=api_key)

def ask_chatgpt(messages):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    response_model = response.model_dump()
    print(json.dumps(response_model, indent=4))
    return response.choices[0].message.content

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is the capital of France?"
    },
    {
        "role": "assistant",
        "content": "The capital of France is Paris"
    },
    {
        "role": "user",
        "content": "Whats is an interesting fact of Paris"
    }
]
response = ask_chatgpt(messages)
print(response)