import logging
import os
from logging import log

KEY = os.environ['OPEN_IA_KEY']
MODEL = os.environ['OPEN_IA_MODEL']

from fastapi import FastAPI, UploadFile
import pdfx
import openai
openai.api_key = KEY

from model.recommed import Recommend
from openia.openia import execute_single_prompt

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload/csv")
async def upload_csv(file: UploadFile):
    file_location = f"{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    text = pdfx.PDFx(file_location).get_text()
    # Modify the text as needed
    text = text.replace('\n\n', ',').strip()  # Remove newlines and strip spaces
    text = text.replace('\n\n\n', '').strip()
    text = text.replace('\n\n\n\n ', '').strip()

    # Save the modified text to a text file
    output_filename = f"HV.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(text)

    return {"info": "file uploaded successfully"}


@app.post('/recommend')
async def recommend(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")
    # Create a prompt for the OpenAI API
    prompt = f"Q: My goad is be a {recommend.recommend}?\n"
    prompt2 = f"Q: Give 4 choices \n"
    # Execute the prompt against the chosen LLM Model
    completion = execute_single_prompt(model=MODEL,
                                       messages=[
                                           {
                                               "role": "user",
                                               "content": f"my hv content {hv_data.read()}"
                                           },
                                           {"role": "user",
                                            "content": prompt
                                            },
                                           {
                                               "role": "system",
                                               "content": "I recommend this carriers fours path for you"
                                           }
                                       ])

    return list(filter(lambda text: text != "", completion.choices[0].message.content.split('\n')))


@app.post('/challenge')
async def challenge(recommend: Recommend):
    prompt = f"Q: If i want to become a {recommend.recommend}?\n"
    # Execute the prompt against the chosen LLM Model
    completion = execute_single_prompt(
        model=MODEL,
        messages=[
            {"role": "user",
             "content": prompt
             },
            {
                "role": "system",
                "content": f"As a system, explain the challenge to the user, tech, business, and people that as a user will face in the future."
                           f"divide in 4 parts, tech, business, and people"
            },

            {
                "role": "assistant",
                "content": "Those will be challenge that you will face in the future"
            }
        ]
    )

    print(completion)
    return {'message': completion.choices[0].message.content}
