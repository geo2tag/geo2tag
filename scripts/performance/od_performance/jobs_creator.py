import requests


def createImportJob(createJobLink, jobData):
    return requests.post(createJobLink, data=jobData)
