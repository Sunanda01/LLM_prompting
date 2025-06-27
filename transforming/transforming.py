import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]

# Translation
# ChatGPT is trained with sources in many languages. This gives the model the ability to do translation. Here are some examples of how to use this capability.

prompt = f"""
Translate the following English text to Hindi: \ 
```Hi, I would like to order an ice cream```
"""
response = get_completion(prompt)
print(response)
# Output= नमस्ते, मुझे एक आइसक्रीम आर्डर करना है।

prompt = f"""
Tell me which language this is: 
```Namaskar, aj apnar din kamon galo?```
"""
response = get_completion(prompt)
print(response)
# Output= This is Bengali language.

prompt = f"""
Translate the following  text to Hindi and Bengali
and English pirate: \
```I want to order a pen```
"""
response = get_completion(prompt)
print(response)
# Output= 
# Hindi: मुझे एक कलम ऑर्डर करनी है।
# Bengali: আমি একটি কলম অর্ডার করতে চাই।
# English: I want to order a pen.

prompt = f"""
Translate the following text to Hindi in both the \
formal and informal forms: 
'Would you like to order a burger?'
"""
response = get_completion(prompt)
print(response)
# Output Formal: क्
# या आप एक बर्गर आर्डर करना चाहेंगे?
# Informal: क्या तुम एक बर्गर आर्डर करना चाहोगे?

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
] 

for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Original message ({lang}): {issue}")

    prompt = f"""
    Translate the following  text to English \
    and Hindi: ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n")
# Output=
# Original message (This is French.): La performance du système est plus lente que d'habitude.
# English: "The system performance is slower than usual."

# Hindi: "सिस्टम का प्रदर्शन सामान्य से धीमा है।" 

# Original message (This is Spanish.): Mi monitor tiene píxeles que no se iluminan.
# English: "My monitor has pixels that do not light up."

# Hindi: "मेरा मॉनिटर पिक्सेल्स जो जलाए नहीं जाते हैं।" 

# Original message (Italian): Il mio mouse non funziona
# English: My mouse is not working
# Hindi: मेरा माउस काम नहीं कर रहा है। 

# Original message (Polish): Mój klawisz Ctrl jest zepsuty
# English: My Ctrl key is broken
# Hindi: मेरा कंट्रोल कुंजी टूट गई है। 

# Original message (This is Chinese.): 我的屏幕在闪烁
# English: My screen is flickering
# Hindi: मेरा स्क्रीन फ्लिकर कर रहा है। 

# Tone Transformation
# Writing can vary based on the intended audience. ChatGPT can produce different tones.
prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)
# Output=
# Dear Sir/Madam,

# I am writing to bring to your attention the specifications of a standing lamp that I believe may be of interest to you. 

# Sincerely,
# Joe

# Format Conversion
# ChatGPT can translate between formats. The prompt should describe the input and output formats.
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)
from IPython.display import display, Markdown, Latex, HTML, JSON
display(HTML(response))

# Spellcheck/Grammar check.
# Here are some examples of common grammar and spelling problems and the LLM's response.
# To signal to the LLM that you want it to proofread your text, you instruct the model to 'proofread' or 'proofread and correct'.
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
    response = get_completion(prompt)
    print(response)

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)

from redlines import Redlines
diff = Redlines(text,response)
display(Markdown(diff.output_markdown))

prompt = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{text}```
"""
response = get_completion(prompt)
display(Markdown(response))

