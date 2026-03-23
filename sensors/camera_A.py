class CameraA:
    def __init__(self, location) -> None:
        self.__location = location
        self.__callback = None

    def on_detect(self, callback):
        self.__callback = callback

    def simulate_detection(self):
        if self.__callback:
            message = f"Camera A: mouvement detecté dans `{self.__location}`"
            self.__callback(message)
                 
