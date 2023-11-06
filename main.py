import logging
import os
import re

from starlette.middleware.cors import CORSMiddleware

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
        },
        {
            "name": "get_skills",
            "description": "Get a list of skills in the text, like nodejs, programming, leadership",
            "parameters": {
                "type": "object",
                "properties": {
                    "skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "A list of skills, e.g. ['nodejs', 'programming', 'leadership']"
                    }
                },
                "required": ["skills"]
            }
        }
    ]
    completion = execute_single_prompt_with_functions(model=MODEL,
                                                      messages=[
                                                          {
                                                              "role": "user",
                                                              "content": f"my hv content {text}"
                                                          },

                                                      ],
                                                      functions=functions,
                                                      )
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
    completion = execute_single_prompt(
        model=MODEL,
        messages=[

            {
                "role": "user",
                "content": f"According with my HV and desired jobs, could you recommend me a few poistions"
            },
            {
                "role": "system",
                "content": "I would you recommend this jobs for you"
            }
        ]
    )
    return completion
