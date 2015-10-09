from geocoding_job import GeocodingJob
import sys
sys.path.append('../')
sys.path.append('/var/www/geomongo/open_data_import')
from job_list_resource_factory import JobListResourceFactory


class GeocodingJobListResource(JobListResourceFactory(None, GeocodingJob, None)):
    pass
