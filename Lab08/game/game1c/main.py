# main.py
from world import Spot
from character import Player, Enemy


alkirasc = Spot('Alkira Secondary College', 'A lot of kids spend their lives here.')
daveshome = Spot("Dave's Home", "It is a dark house and a bad smell comes out from it.")
alkirasc.connect(daveshome, 'south')
daveshome.connect(alkirasc, 'north')

#player_name = input('Name of the Great Adventure please: ')
player_name = 'Jeremy'
player = Player(player_name, alkirasc)

dave = Enemy('Dave', 'A smelly zombie.', 'garlic')
dave.conversation = 'I like to eat humans.'
steve = Enemy('Steve', 'A shifty ghost.', 'cake')
steve.conversation = "This doesn't look good, dude."
daveshome.add_characters(dave)
daveshome.add_characters(steve)


def who(command):
    commands = command.split()
    if len(commands) == 1:
        return player.current_spot.characters[0]
    elif len(commands) == 2:
        for character in player.current_spot.characters:
            if character.name.lower() == commands[1].lower():
                return character


while True:
    print("\n")
    player.current_spot.show()
    player.hud()
    command = input(">>> ")
    if command.strip() == "bye":
        print("Farewell, my hero.")
        break
    elif command.strip() == "":
        continue
    elif command in ['north', 'south', 'east', 'west']:
        player.current_spot = player.current_spot.move(command)
    elif command.startswith('talk'):
        who(command).talk()
    elif command.startswith('fight'):
        if not who(command).fight('fists'): # lost
            player.health -= 1

