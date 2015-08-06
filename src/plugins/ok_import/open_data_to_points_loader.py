import sys
sys.path.append('../..')
from db_model import getDbObject
serviceName = 'testservice'
POINTS = 'points'
class OpenDataToPointsLoader:
    pointsArray = []
    def __init__(self, points):
        self.pointsArray = points

    def loadPoints(self):
        collection = getDbObject(serviceName)[POINTS]
        for point in self.pointsArray:
            collection.save(point)