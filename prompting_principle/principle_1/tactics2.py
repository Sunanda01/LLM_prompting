# Tactic 2: Ask for a structured output
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)

# Output
# [
#     {
#         "book_id": 1,
#         "title": "The Midnight Garden",
#         "author": "Elena Rivers",
#         "genre": "Fantasy"
#     },
#     {
#         "book_id": 2,
#         "title": "Echoes of the Past",
#         "author": "Nathan Black",
#         "genre": "Mystery"
#     },
#     {
#         "book_id": 3,
#         "title": "Whispers in the Wind",
#         "author": "Samantha Reed",
#         "genre": "Romance"
#     }
# ]