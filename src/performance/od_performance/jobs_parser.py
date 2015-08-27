import requests
import json

DONE = 'done'
VALUE = 'value'
TIME = 'time'
JOBS_LIST = {'average': {}, 'min': {}, 'max': {}}
def getImportJobsText(viewJobsLink):
    return requests.get(viewJobsLink).text

def parseJobs(jobsText):
    return json.loads(jobsText)

def areAllJobsDone(jobsList):
    for job in jobsList:
        if job.get(DONE) == False:
            return False
    return True

def createJobStatistic(jobsList):
    minValue = maxMalue = averageValue = summ = 0
    for i in range(len(jobsList)):
        if i == 0:
            minValue = jobsList[i].get(TIME)
            maxValue = jobsList[i].get(TIME)
        if jobsList[i] > maxValue:
            maxValue = jobsList[i].get(TIME)
        if jobsList[i] < minValue:
            minValue = jobsList[i].get(TIME)
        summ += jobsList[i]
    