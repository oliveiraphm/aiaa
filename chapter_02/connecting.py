import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

client = OpenAI(api_key=api_key)

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
    )
    return response.choices[0].message.content

user = "What is teh capital of France?"
response = ask_chatgpt(user)
print(response) 