import threading
class ThreadJob():
    
    def __init__(backgroundFunction, channelName, openDataUrl, showObjectUrl, showImageUrl):
        self.thread = None
        self._id = generateId()
        self.startTime = None
        self.done = False
        self.timeElapsed = None 
        self.backgroundFunction = backgroundFunction
        self.channelName = channelName
        self.openDataUrl = openDataUrl
        self.showObjectUrl = showObjectUrl
        self.showImageUrl = showImageUrl
    
    def internalStart(self):
        thread = threading.Thread(self.backgroundFunction(), args=(channelName, openDataUrl, showObjectUrl, showImageUrl, ))
        thread.start()

    def internalStop(self):
        thread.join()
    
    def start(self):
        self.startTime = datetime.now()
        self.internalStart()
    
    def stop(self):
        self.internalStop()
        self.done = True
        self.timeElapsed = self.startTime - datetime.now()
    
    
    def getTimeStatistics(self):
        if self.timeElapsed == None:
            return self.startTime - datetime.now()
        return self.timeElapsed
    
    def describe(self):
        print { '_id': self._id, 'time': self.getTimeStatistics().toString(), 'done': self.done, 'channelName': self.channelName, 'openDataUrl': self.openDataUrl, 'showObjectUrl', 'showImageUrl': self.showImageUrl}
    
    @classmethod
    def generateId(cls):
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(12))