import requests
import json
from datetime import datetime
import string

AVERAGE = 'average'
DONE = 'done'
VALUE = 'value'
TIME = 'time'
MIN = 'min'
MAX = 'max'
JOB = 'job'
JOBS_LIST = {
    'average': {
        'value': {}}, 'min': {
            'value': {}, 'job': {}}, 'max': {
                'value': {}, 'job': {}}}


def timeConvert(data):
    return string.zfill(str(data / 3600000000),
                        1) + ':' + string.zfill(str(data / 60000000),
                                                2) + ':' + string.zfill(str(data / 1000000),
                                                                        2) + '.' + str(data)[:6]


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
    summ = 0
    for i in range(len(jobsList)):
        jobTime = jobsList[i].get(TIME)
        timeObj = datetime.strptime(jobTime, "%H:%M:%S.%f")
        summ += int(timeObj.strftime("%f")) + (int(timeObj.strftime("%S")) + int(
            timeObj.strftime("%M")) * 60 + int(timeObj.strftime("%H")) * 3600) * 1000000
        if i == 0:
            minValue = timeObj
            maxValue = timeObj
        if timeObj > maxValue:
            maxValue = timeObj
        if minValue > timeObj:
            minValue = timeObj
    JOBS_LIST[AVERAGE][VALUE] = timeConvert(summ / len(jobsList))
    JOBS_LIST[MIN][VALUE] = minValue.strftime("%H:%M:%S.%f")
    JOBS_LIST[MIN][JOB] = jobsList
    JOBS_LIST[MAX][VALUE] = maxValue.strftime("%H:%M:%S.%f")
    JOBS_LIST[MAX][JOB] = jobsList
    return JOBS_LIST
