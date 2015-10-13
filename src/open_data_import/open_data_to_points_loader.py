from db_model import getDbObject
POINTS = 'points'


class OpenDataToPointsLoader:
    pointsArray = []

    def __init__(self, serviceName, points):
        self.pointsArray = points
        self.serviceName = serviceName

    def loadPoints(self):
        collection = getDbObject(self.serviceName)[POINTS]
        for point in self.pointsArray:
            collection.save(point)
