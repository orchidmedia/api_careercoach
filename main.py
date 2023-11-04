import logging
import os

KEY = os.environ['OPEN_IA_KEY']
MODEL = os.environ['OPEN_IA_MODEL']

import pdfx

from fastapi import FastAPI, UploadFile

from model.recommed import Recommend
from openia.openia import execute_single_prompt

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    logger.info("Hellow world")
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
    os.remove(file_location)
    return {"info": "file uploaded successfully"}


@app.post('/career')
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
                                               "content": "I recommend this 4 carrier path for you"
                                           }
                                       ])

    return list(filter(lambda text: text != "", completion.choices[0].message.content.split('\n\n')))


@app.post('/recommend')
async def challenge(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")
    # Execute the prompt against the chosen LLM Model
    completion = execute_single_prompt(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"my hv content {hv_data.read()}"
            },
            {"role": "assistant",
             "content": "Based in the previus message, I recommend this 4 carrier path for you"
             },
            {
                "role": "system",
                "content": "I would like to recommend this 4 carrier path for you"
            }
        ]
    )

    print(completion)
    return {'message': completion.choices[0].message.content}
