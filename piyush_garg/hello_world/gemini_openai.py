# from dotenv import load_dotenv
from openai import OpenAI  # OpenAI SDK

# load_dotenv

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only ans maths related questions. That if the query is not relates to maths. Just say sorry and do not answer that"},
        {"role": "user", "content": "Hey, Can you help me to solve a + b whole square"}
    ]
)

print(response.choices[0].message.content)
