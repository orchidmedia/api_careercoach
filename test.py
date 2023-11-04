response = {
    "id": "chatcmpl-8HDklB6Z6xvmLhVJLOKJHeHwBISRz",
    "object": "chat.completion",
    "created": 1699115135,
    "model": "ft:gpt-3.5-turbo-0613:orchid-media::8FvZOXX3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "1. Build a strong technical foundation: Start by gaining expertise in programming languages, databases, cloud platforms, and software development methodologies.\n\n2. Expand your leadership skills: Take courses or workshops focused on leadership, team management, and effective communication.\n\n3. Gain project management experience: Look for opportunities to lead technical projects and learn project planning, resource allocation, and risk management.\n\n4. Seek leadership roles: Apply for positions that require technical leadership, such as a tech lead or engineering manager, and highlight your experience and skills in this area.\n\nRemember to constantly improve your technical knowledge, stay updated with industry trends, and develop a vision for technical innovation."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 1446,
        "completion_tokens": 129,
        "total_tokens": 1575
    }
}

print(response['choices'][0]['message']['content'].split('\n\n'))