class Spot:
    def __init__(self, name, info=""):
        self.name = name
        self.info = info
        self.next_spots = {}
        self.characters = []


    def connect(self, next_spot, direction):
        self.next_spots[direction] = next_spot

    def show(self):
        print(self.name)
        print("-" * len(self.name))
        print(self.info)
        for character in self.characters:
            character.about()

        for direction in self.next_spots:
            print("🏃 The " + self.next_spots[direction].name + " is " + direction + '.')

    def move(self, direction):
        if direction in self.next_spots:
            return self.next_spots[direction]
        else:
            print(">>> You can't go that way.\n")
            return self

    def add_characters(self, *characters):
        for c in characters:
            self.characters.append(c)

# \|/-*-/|\ links
# opposites = {
#     "east": "west",
#     "west": "east",
#     "south": "north",
#     "north": "south",
#     "southeast": "northwest",
#     "southwest": "northeast",
#     "northeast": "southwest",
#     "northwest": "southeast"
# }