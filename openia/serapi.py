import os

from serpapi import GoogleSearch


def search_job(query: str, location: str):
    params = {
        "api_key": os.getenv('SEARCH_JOB_API_KEY'),
        "engine": "google_jobs",
        "google_domain": "google.com.co",
        "q": query,
        "hl": "en",
        "location": location,
        "start": "4"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    results['jobs_results'] = results['jobs_results'][:4]
    return results
