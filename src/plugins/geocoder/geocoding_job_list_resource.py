from geocoding_job import GeocodingJob
from job_list_resource_factory import JobListResourceFactory


class GeocodingJobListResource(
    JobListResourceFactory(
        None,
        GeocodingJob,
        None)):
    pass
