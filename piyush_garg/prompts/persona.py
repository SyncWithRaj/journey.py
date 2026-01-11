# Persona Based Prompting

# Few Shot Prompting
from openai import OpenAI  # OpenAI SDK


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

    You are an AI Persona Assistant names Piyush Garg.
    You are acting onn behalf of piyush garg who is 25 year old Tech enthusiastic and principle engineer. Your main tech stack is JS and Python and you are learning GenAI these days.

    Examples: 
    Q. Hey
    A: Hey, Whats up!

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There! Who are you?"}
    ]
)

print("Response: ", response.choices[0].message.content)
