import json
import os
import re

from openia.openia import execute_single_prompt, execute_single_prompt_with_model


class RecommendationService:
    def __init__(self, key, model):
        self.key = os.environ['OPEN_IA_KEY']
        self.model = os.environ['OPEN_IA_MODEL']
        pass

    def get_recommendations_from_csv(self, text):
        completion = execute_single_prompt_with_model(model=self.model,
                                                      messages=[
                                                          {
                                                              "role": "user",
                                                              "content": f"my hv content {text}"
                                                          },
                                                          {"role": "user",
                                                           "content": f'Based on my HV text, can you recommend me 4 jobs?'
                                                           },
                                                          {
                                                              "role": "user",
                                                              "content": "Use format with bullets to separate the jobs, "
                                                                         "for example: \n\n - Software Engineer \n - Data "
                                                                         "Scientist \n - Data Engineer \n - Data Analyst"
                                                          }
                                                      ])
        response = completion.choices[0].message.content
        response = list(map(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x), response.split('\n')))
        file_location = f"recommendation_job.json"
        with open(file_location, "wb+") as file_object:
            file_object.write(json.dumps(response).encode())
        return response
