import os

from serpapi import GoogleSearch


def search_job(params):
    params['api_key'] = os.getenv('SEARCH_JOB_API_KEY')
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
