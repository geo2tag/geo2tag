from geocoding_job import GeocodingJob
import sys
sys.path.append('../')
sys.path.append('/var/www/geomongo/open_data_import')
from job_list_resource_factory import JobListResourceFactory

JobListResource = JobListResourceFactory(None, GeocodingJob, None)
