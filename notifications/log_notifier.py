from base_notifier import BaseNotifier

class LogNotifier(BaseNotifier):
    def __init__(self) -> None:
        pass

    def notify(self):
        print("notify log")

