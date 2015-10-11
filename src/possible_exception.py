from base_geo2tag_exception import BaseGeo2TagException

def possibleException(func):
    def funcPossibleException(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseGeo2TagException as e:
            if hasattr(e, 'getReturnObject'):
                return e.getReturnObject()
            else:
                raise
    return funcPossibleException
