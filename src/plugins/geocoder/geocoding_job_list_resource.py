from geocoding_job import GeocodingJob
from job_list_resource_factory import JobListResourceFactory
from geocoding_parser import GeocodingParser
from geocoder_import import geocoderImport


class GeocodingJobListResource(
    JobListResourceFactory(
        GeocodingParser,
        GeocodingJob,
        geocoderImport)):
    pass
