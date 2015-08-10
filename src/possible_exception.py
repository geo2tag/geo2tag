def possibleException(func):
    def funcPossibleException(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if hasattr(e, 'getReturnObject'):
                return e.getReturnObject()
            else:
                raise
    return funcPossibleException
