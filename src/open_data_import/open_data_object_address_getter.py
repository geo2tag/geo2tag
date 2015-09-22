from abc import ABCMeta, abstractmethod

class OpenDataObjectAddressGetter():
    __metaclass__=ABCMeta

    @abstractmethod
    def getAddress(self, obj):
        pass

    def getAddressList(self, objList) :
        return [self.getAddress(x) for x in objList]