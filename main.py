import json
import logging
import os
import re

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile

import utils
from openia.pdf import text_from_pdf
from openia.serapi import search_job
from services.services import RecommendationService

KEY = os.environ['OPEN_IA_KEY']
MODEL = os.environ['OPEN_IA_MODEL']

from model.recommed import Recommend
from openia.openia import execute_single_prompt, execute_single_prompt_with_functions, execute_single_prompt_with_model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)
logger = logging.getLogger(__name__)

REGEX_TITLES = r'\d+\.\s([^:]+):'

recommendation_service = RecommendationService(key=KEY, model=MODEL)


@app.get("/")
async def root():
    logger.info("Hellow world")
    return {"message": "Hello World"}

# Upload CV process
@app.post("/upload/csv")
async def upload_csv(file: UploadFile):
    file_location = f"{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    text = text_from_pdf(file_location)

    # Save the modified CV to a text file
    output_filename = f"HV.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(text)
    os.remove(file_location)
    return recommendation_service.get_recommendations_from_csv(text)
    # return {"message": "File uploaded successfully"}


@app.post('/career')
async def recommend(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")
    recommend_jobs = open("recommendation_job.json", "r", encoding="utf-8")
    recommend_jobs = json.loads(recommend_jobs.read())
    completion = execute_single_prompt_with_model(model=MODEL,
                                       messages=[
                                           {
                                               "role": "user",
                                               "content": f"my hv content {hv_data.read()}"
                                           },
                                           {
                                               "role": "system",
                                               "content": f'Take notes based on the career path that suggested {recommend_jobs}'
                                           },
                                           {
                                                "role": "user",
                                                "content": f'I would like to be a {recommend.recommend}'
                                            },
                                           {
                                                "role": "system",
                                                "content": "Based career path selected, list me the Soft Skills, Hard Skills, Challenges, Advantages, Disadvantages and Nice-To-Have for the career path. Please do it in an orginize list with tile and description"  
                                            },
                                            {
                                                "role": "user",
                                                "content": "Use json format key title as string to describe item and"
                                                "description as a array of strings example [{\"title\":\"title\", \"description\":[\"description1\", \"description2\"]}]"
                                            },

                                       ])
    response = completion.choices[0].message.content

    return json.loads (response)
#utils.extract_carrer_path_challenges(response)


@app.post('/recommend')
async def challenge(recommend: Recommend):
    hv_data = open("HV.txt", "r", encoding="utf-8")

    # Execute the prompt against the chosen LLM Model
    completion = execute_single_prompt_with_model(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"this is my resume or cv content {hv_data.read()}"
            },
            {
                "role": "user",
                "content": f'This is the career path recommendation {recommend.recommend}'
            },
            {
                "role": "user",
                "content": "Use format with bullets to separate the jobs, "
                           "for example: \n\n - Software Engineer: long description of this carrier. \n - Data "
                           "Scientist: long description of this carrier."
            },
            {"role": "system",
             "content": "Based in the previous message, recommend 4 ideal professional career paths"
             },
            {
                "role": "assistant",
                "content": "I would like to recommend this 4 career path for you"
            }
        ]
    )

    messages = completion.choices[0].message.content
    return utils.extract_recommend(messages)


@app.post('/search-career')
async def search_career(recommend: Recommend):
    return search_job(recommend.recommend, 'United States')
