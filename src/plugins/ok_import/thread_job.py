import threading
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

    def describe(self):
        ancestorResult = Job.describe(self)
        ancestorResult[showImageUrl] = self.importDataDict.get(showImageUrl)
        ancestorResult[showObjectUrl] = self.importDataDict.get(showObjectUrl)
        return ancestorResult
