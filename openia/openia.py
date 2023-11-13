import os
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv('OPEN_IA_KEY'),
)

#This executes the first endpoint which loads, read the resume and generates the 4 recommendations
def execute_single_prompt_with_model(model: str, messages: list[dict]):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=2048
        # token_max_length=500,
    )
    print(completion.choices[0].message.content)
    return completion


def execute_single_prompt(model: str, messages: list[dict]):
    completion = client.chat.completions.create(
        model='gpt-4',
        messages=messages,
        max_tokens=2048
        # token_max_length=500,
    )
    print(completion.choices[0].message.content)
    return completion


def execute_single_prompt_with_functions(model: str, messages: list[dict], functions: list[dict]):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.9,
        max_tokens=2048,
        functions=functions,
        function_call="auto",
        # token_max_length=500,
    )
    return completion
