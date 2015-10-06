import threading
import sys
import os
sys.path.append('/var/www/geomongo/open_data_import')
from job import Job

OPEN_DATA_URL = 'openDataUrl'

class GeocodingJob(Job):

    def internalStart(self):
        thread = threading.Thread(
            target=self.backgroundFunction,
            args=(
                self,
                self.channelName,
                self.serviceName
            )
        )
        self.thread = thread
        thread._stop = threading.Event()
        thread.start()

    def internalStop(self):
        self.thread.join()

    def describe(self):
        ancestorResult = Job.describe(self)
        ancestorResult.pop(OPEN_DATA_URL)
        return ancestorResult
