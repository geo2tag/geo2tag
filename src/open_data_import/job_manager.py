class JobManager:
    jobs = {}

    @classmethod
    def startJob(cls, job):
        jobId = job.describe()['_id']
        job.start()
        cls.jobs[jobId] = job
        return jobId

    @classmethod
    def getJob(cls, jobId):
        return cls.jobs.get(jobId).describe()

    @classmethod
    def stopJob(cls, jobId):
        cls.jobs.get(jobId).stop()

    @classmethod
    def getJobs(cls):
        result = []
        for job in cls.jobs:
            result.append(cls.jobs[job].describe())
        return result
