class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def describe(self):
        print(f"Here is {self.name}; {self.description}")

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def show(self):
        print(self.name)            # answer
        print("-" * len(self.name)) # answer
        print(self.description)     # answer
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self