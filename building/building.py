class Building
    def __init__(self, name) -> None:
        self.__name = name
        self.__rooms = []

    def add_room(self, room):
        self.__rooms.append(room)

    def get_room(self, name):
        for room in self.__rooms:
            if room.get_name() == name:
                return room

        return None

    def get_rooms_list(self):
        return [room.get_name() for room in self.__rooms]
