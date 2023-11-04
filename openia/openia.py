# Executes a single prompt against the chosen LLM Model
from langchain.adapters import openai

def execute_single_prompt(model:str,messages:list[dict]):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
        max_tokens=1024
        # token_max_length=500,
    )
    return completion
