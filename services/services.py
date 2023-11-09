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
                                                           "content": f'Based on my HV text, can you recommend me 4 '
                                                                      f'jobs?'
                                                           },
                                                          {
                                                              "role": "user",
                                                              "content": "Use json format key title as string to describe item and "
                                                                         "description as a array of strings"
                                                          },

                                                      ])

        response = json.loads(completion.choices[0].message.content)
        values = list(response.values())
        if type(values[0])==list:
            values = values[0]

        keys = list(map(lambda x: x['title'], values))
        file_location = f"recommendation_job.json"
        with open(file_location, "wb+") as file_object:
            file_object.write(json.dumps(keys).encode())
        return values
