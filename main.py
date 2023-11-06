import json
import logging
import os
import re

from starlette.middleware.cors import CORSMiddleware

from openia.serapi import search_job

KEY = os.environ['OPEN_IA_KEY']
MODEL = os.environ['OPEN_IA_MODEL']

import pdfx

from fastapi import FastAPI, UploadFile

from model.recommed import Recommend
from openia.openia import execute_single_prompt, execute_single_prompt_with_functions

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)
logger = logging.getLogger(__name__)

REGEX_TITLES = r'\d+\.\s([^:]+):'


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
    return {"message": "File uploaded successfully"}


@app.post('/career')
async def recommend(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")
    completion = execute_single_prompt(model=MODEL,
                                       messages=[
                                           {
                                               "role": "user",
                                               "content": f"my hv content {hv_data.read()}"
                                           },
                                           {"role": "user",
                                            "content": f'be a {recommend.recommend}'
                                            },
                                           {
                                               "role": "user",
                                               "content": """
                                               As user i would like to know the career path for this 
                                               job, divide the text in titles separate from content with : and 
                                               subtitles start with - and end with ; with numerals and :
                                               Tell me description about skills required soft and tech, nice to have, 
                                               challenges, advantages disadvantage, how i can learn and grow to reach 
                                               this job, be more specific and detailed
                                               """
                                           },

                                       ])
    response = completion.choices[0].message.content
    print('openia')

    # Define regular expressions for titles, subtitles, and content
    title_pattern = r'\n- (.*?):'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    titles = titles[1:]

    description = r'^\d+\.\s(.*?\.)$'
    body = []

    for i, title in enumerate(titles):
        # print(title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)

        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()

    return body


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

    messages = completion.choices[0].message.content
    descriptions = messages.split('\n\n')
    # Buscar los títulos en el texto
    titles = re.findall(REGEX_TITLES, messages)
    response = []
    for title in range(0, len(titles)):
        response.append({
            "title": titles[title],
            "description": descriptions[title + 1].replace(titles[title], '')
        })
    return response


@app.post('/search-career')
async def search_career(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")
    functions = [
        {
            "name": "get_location",
            "description": "Get the city and country from the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city, e.g. Bogota",
                    },
                    "country": {
                        "type": "string",
                        "description": "The country, e.g. Colombia",
                    },
                },
                "required": ["country"],
            },
        }
    ]
    completion = execute_single_prompt_with_functions(model=MODEL,
                                                      messages=[
                                                          {
                                                              "role": "user",
                                                              "content": f"my hv content {hv_data.read()}"
                                                          },
                                                      ],
                                                      functions=functions,
                                                      )
    print(completion.choices[0].message)

    location = json.loads(completion.choices[0].message.function_call.arguments)
    return search_job(recommend.recommend, location['country'])
