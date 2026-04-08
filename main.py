import os
from dotenv import load_dotenv
import sys
from groq import Groq
from functions.get_files_from_directory import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

def talk_to_llm(prompt: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt,
            },
        ],
        model="llama-3.3-70b-versatile",
    )

    # print(chat_completion.choices[0].message.content)
    for chat_response in chat_completion.choices:
        print(chat_response.message.content)

def main():
    prompt = ''
    while prompt != 'exit':
        prompt = input('Type your prompt: ')
        talk_to_llm(prompt)
        print('\n\n')

# main()
print(write_file("calculator", "test.txt", "ola mundo"))
