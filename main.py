import logging
import os
from logging import log

from fastapi import FastAPI, UploadFile
import pdfx
import openai

from model.recommed import Recommend

KEY = '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'
openai.api_key = KEY

MODEL = 'ft:gpt-3.5-turbo-0613:orchid-media::8FvZOXX3'
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
    print(hv_data.read())
    # Create a prompt for the OpenAI API
    prompt = f"Q: My goad is be a {recommend.recommend}?\n"
    prompt2 = f"Q: Give 4 choices \n"
    ##
    # Execute the prompt against the chosen LLM Model
    completion = openai.ChatCompletion.create(
        model=MODEL,
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
            },

        ],
        temperature=0.9,
    )

    # Return the result
    return completion
