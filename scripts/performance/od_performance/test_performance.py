#!/usr/bin/env python
from jobs_creator import createImportJob
from jobs_parser import createJobStatistic, parseJobs, getImportJobsText, areAllJobsDone
import time
from requests.exceptions import ConnectionError

CREATE_JOB_LINK = '-createJobLink'
JOB_DATA = '-jobData'
VIEW_JOB_LINK = '-viewJobsLink'
JOB_COUNT = '-jobsCount'
TIMEOUT = '-timeout'
DEFAULT_JOB_COUNT = 1
DEFAULT_TIMEOUT = 60


def main(createJobLink, jobData, viewJobsLink, jobsCount, timeout):
    try:
        for _ in range(0, jobsCount):
            createImportJob(createJobLink, jobData)
    except ConnectionError:
        print "Connection to" + createJobLink + " not works"
        return 1
    time.sleep(timeout)
    jobsText = getImportJobsText(viewJobsLink)
    jobsList = parseJobs(jobsText)
    if not areAllJobsDone(jobsList) or len(jobsList) == 0:
        print "No results by timeout"
        return 1
    else:
        print createJobStatistic(jobsList)
        return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(CREATE_JOB_LINK, type=str, required=True)
    parser.add_argument(JOB_DATA, type=str, required=True)
    parser.add_argument(VIEW_JOB_LINK, type=str, required=True)
    parser.add_argument(JOB_COUNT, type=int, default=DEFAULT_JOB_COUNT)
    parser.add_argument(TIMEOUT, type=int, default=DEFAULT_TIMEOUT)
    args = parser.parse_args()
    main(
        args.createJobLink,
        args.jobData,
        args.viewJobsLink,
        args.jobsCount,
        args.timeout)
