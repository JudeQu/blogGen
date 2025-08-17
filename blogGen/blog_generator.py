from openai import OpenAI
from dotenv import dotenv_values

# Load API key from .env
config = dotenv_values(".env")
client = OpenAI(api_key=config["API_KEY"])

def generate_blog(topic):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Write me a blog that summarizes the following topic: " + topic}
        ],
        max_tokens=450,
        temperature=0.3
    )
    return response.choices[0].message.content

keep_blogging = True
while keep_blogging:
    answer = input("Write a summary? Y for yes, anything else for no\n")
    if answer == 'Y' or answer == 'y':
        blog = input("What topic would you like a summary of?\n")
        print(generate_blog(blog))
    else:
        keep_blogging = False




