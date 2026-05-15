class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    def set_rooms(self, new_rooms):
        if new_rooms > 0:
            self.__rooms = new_rooms
        else:
            print("Xonalar soni xato")


h1 = Hospital("Shifo", 50)

print(h1.name)
print(h1.get_rooms())

h1.set_rooms(80)
print(h1.get_rooms())

h1.set_rooms(0)
