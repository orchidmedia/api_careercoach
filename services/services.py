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
                                                           "content": 'Based on my resume text, please give me 4 clear recommendations to improve my resume. Be specific with titles and descriptions of each recommendation, and again, only 4 recommendations'
                                                           },
                                                          {
                                                              "role": "user",
                                                              "content": "Use json format key title as string to describe item and "
                                                                         "description as a array of strings example [{\"title\":\"title\", \"description\":[\"description1\", \"description2\"]}]"
                                                          },

                                                      ])

        response = json.loads(completion.choices[0].message.content)

        keys = list(map(lambda x: x['title'], response))
        file_location = f"recommendation_job.json"
        with open(file_location, "wb+") as file_object:
            file_object.write(json.dumps(keys).encode())
        return response
