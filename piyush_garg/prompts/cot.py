# Chain of Thought (CoT) for Reasoning
from openai import OpenAI  # OpenAI SDK
import json

client = OpenAI(
    api_key="AIzaSyB1tbsBCwUanNG9XjRoZyEvQohOERHXpss",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thoughts.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN What needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output formate
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON Format: { "step: "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example: 
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in maths problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" 
    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" 
    PLAN: { "step": "PLAN", "content": "first the must multiply 3 * 5 which is 15" 
    PLAN: { "step": "PLAN", "content": "Now the new euatin is 2 + 15 / 10" 
    PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5" 
    PLAN: { "step": "PLAN", "content": "Now the ne equation is 2 + 1.5" 
    PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5" 
    PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans" 
    PLAN: { "step": "PLAN", "content": "3.5" 
    }
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in js"},
        # Manually keep adding messages to History
        {"role": "assistant", "content": json.dumps({"role": "START","content": "You want a JavaScript code to add 'n' numbers."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a JavaScript function to add an arbitrary number of inputs ('n' numbers)."})},
        {"role": "assistant", "content": json.dumps({
  "step": "PLAN",
  "content": "I will define a JavaScript function that uses the rest parameter (...) to accept an arbitrary number of arguments. Inside the function, I'll initialize a sum to zero and then iterate through the arguments, adding each one to the sum. Finally, I'll return the total sum and provide an example of its usage."
})},
        {"role": "assistant", "content": json.dumps({
  "step": "OUTPUT",
  "content": "```javascript\nfunction addNumbers(...numbers) {\n  let sum = 0;\n  for (const number of numbers) {\n    sum += number;\n  }\n  return sum;\n}\n\n// Example Usage:\nconsole.log(addNumbers(1, 2, 3));         // Output: 6\nconsole.log(addNumbers(10, 20, 30, 40));  // Output: 100\nconsole.log(addNumbers(5));               // Output: 5\nconsole.log(addNumbers());                // Output: 0\nconsole.log(addNumbers(1.5, 2.5, 3));     // Output: 7\n```"
})}
    ]
)

print(response.choices[0].message.content)