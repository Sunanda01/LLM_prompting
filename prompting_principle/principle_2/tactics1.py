# Tactic 1: Specify the steps required to complete a task
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

text = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""

# example 1
prompt_1 = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into Bengali.
3 - List each name in the Hindi summary.
4 - Output a json object that contains the following \
keys: hindi_summary, names.

Separate your answers with line breaks.

Text:
```{text}```
"""
response = get_completion(prompt_1)
print("Completion for prompt 1:")
print(response)

# Output
# Completion for prompt 1:
# 1 - Jack and Jill, siblings from a charming village, go on a quest to fetch water from a hilltop well, but encounter misfortune along the way.

# 2 - একটি মোহনীয় গ্রামে, ভাই-বোন জ্যাক এবং জিল একটি পাহাড়ের উপর থেকে পানি নিয়ে আসতে যান, তবে পথে দুর্ভাগ্যের সম্মুখীন হয়।

# 3 - जैक, जिल

# 4 - 
# {
#   "hindi_summary": "एकटी मोहनीय ग्राम में, भाई-बहन जैक और जिल एक पहाड़ी कुए से पानी लाने के लिए निकलते हैं, लेकिन रास्ते में दुर्भाग्य से भिड़ जाते हैं।",
#   "names": ["जैक", "जिल"]
# }

prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into korean.
3 - List each name in the korean summary.
4 - Output a json object that contains the 
  following keys: korean_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
response = get_completion(prompt_2)
print("\nCompletion for prompt 2:")
print(response)

# Output
# Completion for prompt 2:
# Summary: Jack and Jill, siblings, go on a quest to fetch water but encounter misfortune along the way, yet their adventurous spirits remain undimmed.

# Translation: 잭과 질, 형제, 물을 가져 오기 위해 여행을 떠나지만 중간에 불행을 만나지만 그들의 모험 정신은 여전히 사그라들지 않습니다.

# Names: 잭, 질

# Output JSON: 
# {
#   "korean_summary": "잭과 질, 형제, 물을 가져 오기 위해 여행을 떠나지만 중간에 불행을 만나지만 그들의 모험 정신은 여전히 사그라들지 않습니다.",
#   "num_names": 2
# }