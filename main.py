import os
from dotenv import load_dotenv
import sys
from groq import Groq
from functions.get_files_from_directory import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from  functions.run_python_file import run_python_file
import json

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

tools = [
    schema_get_files_info
]

available_functions = {
    "get_files_info": get_files_info,
}

def talk_to_llm(prompt: str):

    system_prompt = """
    You are a helpful AI coding agent.
    When the user asks to perform an action, use the provided tools to execute it.
    If you use a tool, use the tool's output to give a concise and helpful summary to the user.
    All paths should be relative to the current directory.
    """

    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)

            print(f"-- Executing: {function_name}({function_args}) --")
            function_response = function_to_call(
                working_directory=os.getcwd(),
                **function_args
            )

            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response
            })

        second_response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )
        print('Final answer: ', second_response.choices[0].message.content)
    else:
                print("Tool deu ruim")

def main():
    prompt = ''
    while prompt != 'exit':
        prompt = input('Type your prompt: ')
        talk_to_llm(prompt)
        print('\n\n')

main()
