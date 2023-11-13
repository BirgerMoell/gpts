from fastapi import FastAPI, HTTPException
import requests
import random
from search_jobs import remote_jobs_api_search, af_job_search

app = FastAPI()

@app.get("/search_remote_jobs/")
def search_remote_jobs(title: str):
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

@app.get("/search_jobs/")
def search_af_jobs(search_term: str, location: str = "Stockholm"):
    result = af_job_search(search_term, location)
    #result = remote_jobs_api_search(search_term)
    # get all the results
    return result

