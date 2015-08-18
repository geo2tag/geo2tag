import threading
import random
import string
from datetime import datetime


class ThreadJob():

    def __init__(
            self,
            backgroundFunction,
            channelName,
            openDataUrl,
            showObjectUrl,
            showImageUrl,
            serviceName):
        self.thread = None
        self._id = self.generateId()
        self.startTime = datetime.now()
        self.done = False
        self.timeElapsed = None
        self.backgroundFunction = backgroundFunction
        self.channelName = channelName
        self.openDataUrl = openDataUrl
        self.showObjectUrl = showObjectUrl
        self.showImageUrl = showImageUrl
        self.serviceName = serviceName

    def internalStart(self):
        thread = threading.Thread(
            target=self.backgroundFunction,
            args=(
                self.channelName,
                self.openDataUrl,
                self.showObjectUrl,
                self.showImageUrl,
                self.serviceName,
            ))
        self.thread = thread
        thread.start()

    def internalStop(self):
        self.thread.join()

    def start(self):
        self.startTime = datetime.now()
        self.internalStart()

    def stop(self):
        self.internalStop()
        self.done = True
        self.timeElapsed = datetime.now() - self.startTime

    def getTimeStatistics(self):
        if self.timeElapsed is None:
            return datetime.now() - self.startTime
        return self.timeElapsed

    def describe(self):
        return {
            '_id': self._id,
            'time': str(
                self.getTimeStatistics()),
            'done': self.done,
            'channelName': self.channelName,
            'openDataUrl': self.openDataUrl,
            'showObjectUrl': self.showObjectUrl,
            'showImageUrl': self.showImageUrl,
            'serviceName': self.serviceName}

    @classmethod
    def generateId(cls):
        return ''.join(
            random.choice(
                string.ascii_uppercase +
                string.ascii_lowercase +
                string.digits) for x in range(12))
