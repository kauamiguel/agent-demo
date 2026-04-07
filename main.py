import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":"Say hello",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
