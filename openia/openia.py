# Executes a single prompt against the chosen LLM Model
import os

import openai
openai.api_key = os.getenv('OPEN_IA_KEY')
def execute_single_prompt(model:str,messages:list[dict]):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
        max_tokens=1024
        # token_max_length=500,
    )
    return completion
