# main.py
# online demo: https://trinket.io/python/63c3917709?outputOnly=true
#
from room import Room

kitchen = Room("Kitchen")
kitchen.name = "Big Kitchen"
kitchen.description = "A dank and dirty room buzzing with flies. There is a stench of rotten meat."

dining_hall = Room("Dining Hall")
dining_hall.description = "A large room with ornate golden decorations on every wall."

ballroom = Room("Ballroom")
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance"

kitchen.link(dining_hall, "south")
dining_hall.link(kitchen, "north")
dining_hall.link(ballroom, "west")
ballroom.link(dining_hall, "east")

current_room = kitchen

while True:
    print("\n")
    current_room.show()
    command = input("> ")
    if command.strip() == "bye":
        print("Farewell, my hero.")
        break
    elif command.strip() == "":
        continue
    else:
        current_room = current_room.move(command)