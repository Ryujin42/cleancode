from base_notifier import BaseNotifier

class EmailNotifier(BaseNotifier):
    def __init__(self) -> None:
        pass

    def notify(self):
        print("notify email")

