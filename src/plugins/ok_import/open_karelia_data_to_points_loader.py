import sys
sys.path.append('../..')
from db_model import getDbObject
serviceName = 'testservice'
POINTS = 'points'


class OpenKareliaDataToPointsLoader:
    pointsArray = []

    def __init__(self, serviceName, points):
        self.pointsArray = points
        self.serviceName = serviceName

    def loadPoints(self):
        collection = getDbObject(self.serviceName)[POINTS]
        for point in self.pointsArray:
            collection.save(point)
