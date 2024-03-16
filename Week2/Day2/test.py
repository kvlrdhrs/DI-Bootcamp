class Door():
    def __init__(self, is_opened):
        self.is_opened = None

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):
    def open_door(self):
        raise ValueError("Error: A blocked door cannot be opened.")

    def close_door(self):
        raise ValueError("Error: A blocked door cannot be closed.")

