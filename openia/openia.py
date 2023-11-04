# Executes a single prompt against the chosen LLM Model
def execute_single_prompt(prompt, role="system", content_only=True):
    log(logging.DEBUG, f"execute_single_prompt - {prompt}")

    completion = openai.ChatCompletion.create(
        engine=os.environ['OPENAI_MODEL'],
        deployment_id=os.environ['OPENAI_MODEL'],
        messages=[
            {'role': role,
             'content': prompt}
        ],
    )

    log(logging.DEBUG, f"execute_single_prompt result - {completion.choices[0].message['content']}")

    if content_only:
        return completion.choices[0].message['content']
    else:
        return completion
