class TemperatureSensorA:
    def __init__(self, location, threshold) -> None:
        self.__location = location
        self.__threshold = threshold
        self.__callback = None

    def on_detect(self, callback):
        self.__callback = callback

    def simulate_detection(self, current_temp):
        if self.__callback:
            message = f"Temperature sensor A: température de {current_temp}° detectée dans `{self.__location}`, dépassement du seuil `{self.__threshold}`"
            self.__callback(message)
                 
