class BaseError(Exception):
    pass

class GetTaskError(BaseError):
    pass

class GetResultError(BaseError):
    pass

class GetBalanceError(BaseError):
    pass

class UnknownRequestInstanceError(BaseError):
    pass