from typing import Optional

class BaseError(Exception):
    pass

class GetTaskError(BaseError):
    pass

class GetResultError(BaseError):
    pass

class GetBalanceError(BaseError):
    pass

class NumbersImagesErrors(BaseError):
    pass

class ZeroImagesErrors(BaseError):
    pass

class TaskNotDefinedError(BaseError):
    pass

class ExtraParamsError(BaseError):
    pass



class UserAgentNotDefinedError(BaseError):
    
    default_message = 'If "imageUrls" is not defined, then "userAgent" must explicitly specify signature ' \
                      'of a modern browser, otherwise Google will return an error asking you to update your browser.'
    
    def __init__(self, message: Optional[str] = None) -> None:
        self.message = message if message is not None else UserAgentNotDefinedError.default_message
        super().__init__(self.message)

class UnknownRequestInstanceError(BaseError):
    pass
    