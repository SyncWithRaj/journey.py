# from dotenv import load_dotenv
# from openai import OpenAI


# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": "Hey there"}
#     ]
# )

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
   api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
          {
            "role": "user",
            "content": "I am Raj Ribadiya! and Nice to meet you"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)
print(response.choices[0].message.content)
