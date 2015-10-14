import random
import string
from datetime import datetime
from abc import abstractmethod


class Job():

    def __init__(
            self,
            backgroundFunction,
            channelName,
            openDataUrl,
            importDataDict,
            serviceName):
        self.thread = None
        self._id = self.generateId()
        self.startTime = datetime.now()
        self.done = False
        self.timeElapsed = None
        self.backgroundFunction = backgroundFunction
        self.channelName = channelName
        self.openDataUrl = openDataUrl
        self.importDataDict = importDataDict
        self.serviceName = serviceName

    @abstractmethod
    def internalStart(self):
        pass

    @abstractmethod
    def internalStop(self):
        pass

    def start(self):
        self.startTime = datetime.now()
        self.internalStart()

    def stop(self):
        self.timeElapsed = datetime.now() - self.startTime
        self.done = True
        self.internalStop()

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
            'serviceName': self.serviceName}

    @classmethod
    def generateId(cls):
        return ''.join(
            random.choice(
                string.ascii_uppercase +
                string.ascii_lowercase +
                string.digits) for x in range(12))
