class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def describe(self):
        print(f"Here is {self.name}; {self.description}")

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link