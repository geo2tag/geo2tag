import threading
import sys
import os
sys.path.append('/var/www/geomongo/open_data_import')
from job import Job

showImageUrl = 'showImageUrl'
showObjectUrl = 'showObjectUrl'

class ThreadJob(Job):
    
    def internalStart(self):
        thread = threading.Thread(
            target=self.backgroundFunction,
            args=(
                self,
                self.channelName,
                self.openDataUrl,
                self.importDataDict.get(showImageUrl),
                self.importDataDict.get(showObjectUrl),
                self.serviceName,
            ))
        self.thread = thread
        thread.start()
