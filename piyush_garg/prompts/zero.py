# Zero Shot Prompting
from openai import OpenAI  # OpenAI SDK


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero shot prompting: Directly giving the instruction to the model. OR The Model is given a direct question or task without prior examples.
SYSTEM_PROMPT = "You can only and only ans the coding related questions. do not answer anything else. Your name is Alexa. I user asks something other than coding, just say sorry"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you write hello world in C++?"}
    ]
)

print(response.choices[0].message.content)
