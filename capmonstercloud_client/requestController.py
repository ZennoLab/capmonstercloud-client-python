from threading import Timer

class RequestController:
    def __init__(self, timeout: float) -> None:
        self.timeout = timeout
        self.cancel = False
        self.__timer = None

    def __callback(self) -> None:
        self.cancel = True

    def run(self) -> None:
        self.__timer = Timer(self.timeout, self.__callback)
        self.__timer.start()

    def stop(self) -> None:
        if self.__timer is not None:
            self.__timer.cancel()
            self.__callback()