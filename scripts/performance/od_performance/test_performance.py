#!/usr/bin/env python
from jobs_creator import *
from jobs_parser import *
import time
from requests.exceptions import ConnectionError


def main(createJobLink, jobData, viewJobsLink, jobsCount, timeout):
    try:
        for i in range(0, jobsCount):
            createImportJob(createJobLink, jobData)
    except ConnectionError:
        print "Error connection to " +createJobLink
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
    parser.add_argument('-createJobLink', type=str, required=True)
    parser.add_argument('-jobData', type=str, required=True)
    parser.add_argument('-viewJobsLink', type=str, required=True)
    parser.add_argument('-jobsCount', type=int, default=1)
    parser.add_argument('-timeout', type=int, default=60)
    args = parser.parse_args()
    main(args.createJobLink, args.jobData, args.viewJobsLink, args.jobsCount, args.timeout)