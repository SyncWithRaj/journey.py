# Few Shot Prompting
from openai import OpenAI  # OpenAI SDK


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few shot prompting: Directly giving the instructions to the model and few examples to the model related to query
SYSTEM_PROMPT = """
You can only and only ans the coding related questions. do not answer anything else. Your name is Alexa. I user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Outpt Formate:
{{
 "code": "string" or None,
 "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{
 "code": null,
 "isCodingQuestion": false
}}

Q: Hey, Write a code in python for adding two numbers.
A: {{
 "code": "def add(a, b):
       return a + b" or None,
 "isCodingQuestion": true
}}


"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you write hello world in C++?"}
    ]
)

print(response.choices[0].message.content)
