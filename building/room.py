class Room:
    def __init__(self, name) -> None:
        self.__name = name
        self.__sensors = []
        self.__notifiers = []

    def get_name(self):
        return self.__name

    def add_sensor(self, sensor):
        self.__sensors.append(sensor)
        self._subscribe(sensor)

    def add_notifier(self, notifier):
        self.__notifiers.append(notifier)

    def _subscribe(self, sensor):
        if hasattr(sensor, 'on_detect'):
            sensor.on_detect(self._handle_alert)

    def _handle_alert(self, message):
        print(f"Room '{self.__name}' : Alerte reçue : {message}")
        for notifier in self.__notifiers:
            notifier.notify(message)
