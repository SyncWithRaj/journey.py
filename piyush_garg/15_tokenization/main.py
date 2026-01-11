import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text= "Hey there! My name is Piyush Garg"
tokens = enc.encode(text)

print("Tokens", tokens)

decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 398, 3403, 1776, 170676])
print("Decoded", decoded)