import requests
import json
from datetime import datetime
import time
import string
DONE = 'done'
VALUE = 'value'
TIME = 'time'
JOBS_LIST = {'average': {}, 'min': {}, 'max': {}}

def timeConvert(data):
    return string.zfill(str(data/3600000000), 1) + ':' + string.zfill(str(data/60000000), 2) + ':' + string.zfill(str(data/1000000),2) + '.' + str(data)[:6]

def getImportJobsText(viewJobsLink):
    return requests.get(viewJobsLink).text

def parseJobs(jobsText):
    return json.loads(jobsText)

def areAllJobsDone(jobsList):
    print JOBS_LIST1, '***********'
    for job in jobsList:
        if job.get(DONE) == False:
            return False
    return True

def createJobStatistic(jobsList):
    minValue = maxMalue = averageValue = summ = 0
    for i in range(len(jobsList)):
        jobTime = jobsList[i].get(TIME)
        timeObj = datetime.strptime(jobTime, "%H:%M:%S.%f")
        summ += int(timeObj.strftime("%f")) + (int(timeObj.strftime("%S")) + int(timeObj.strftime("%M")) * 60 + int(timeObj.strftime("%H")) * 3600) * 1000000
        if i == 0:
            minValue = timeObj
            maxValue = timeObj
        if timeObj > maxValue:
            maxValue = timeObj
        if minValue > timeObj:
            minValue = timeObj
    JOBS_LIST['average'] = timeConvert(summ/len(jobsList))
    JOBS_LIST['min'] = minValue.strftime("%H:%M:%S.%f")
    JOBS_LIST['max'] = maxValue.strftime("%H:%M:%S.%f")
    return JOBS_LIST