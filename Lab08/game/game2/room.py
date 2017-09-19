class Room():

    def __init__(self, name):

        self.name = name
        self.description = None
        self.linked_rooms = {}

    def link(self, roomToLink, direction):
        self.linked_rooms[direction] = roomToLink

    def show(self):
        print(self.name)
        print("-" * len(self.name))
        print(self.description)
        for direction in self.linked_rooms:
            print( "The " + self.linked_rooms[direction].name+ " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            print("\n")
            return self.linked_rooms[direction]
        else:
            print(">>> You can't go that way\n")
            return self