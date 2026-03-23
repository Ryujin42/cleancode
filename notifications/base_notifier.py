import abc

class BaseNotifier:
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def notify(self):
        print("notification")
