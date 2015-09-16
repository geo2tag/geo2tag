from abc import ABCMeta, abstractmethod
class OpenDataObjectAddressGetter():
    __metaclass__=ABCMeta

    @abstractmethod
    def getAddress(obj):

    def getAddressList(objList) :
    return getAddress(x) for x in objList