import requests
from fastapi import FastAPI, HTTPException
import random

def remote_jobs_api_search(title):
    url = "https://himalayas.app/jobs/api"
    params = {
        "title": title,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error fetching jobs from API")
    response_json = response.json()
    jobs = response_json['jobs']
    # picke one job
    job = random.choice(jobs)
    return job


def af_job_search(search_term, location):
    headers = {
        'accept': 'application/json',
        'x-feature-freetext-bool-method': 'or',
    }

    params = {
        'q': search_term,
        'offset': '0',
        'limit': '100',
        'l': location,
    }

    response = requests.get('https://jobsearch.api.jobtechdev.se/search', params=params, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error fetching jobs from API")

    response_json = response.json()
    jobs = response_json.get('hits', [])
    
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")

    # get the first five jobs
    jobs = jobs[:5]

    job = random.choice(jobs)
    result = {
        "headline": job['headline'],
        "logo_url": job.get('logo_url', ''),
        "description": job['description']['text'],
        "webpage_url": job['webpage_url']
    }

    # get all the results

    return jobs

# search the following url
# jobs = search_remote_jobs("Software Engineer")
# print("jobs: ", jobs)
