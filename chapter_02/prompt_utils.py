from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def prompt_llm(messages, model='gpt-3.5-turbo', base_url=None, api_key=""):
    if base_url:
        client = OpenAI(base_url=base_url, api_key=api_key)
    else:
        client = OpenAI()

    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temprature = 0.7,
    )

    return response.choices[0].message.content