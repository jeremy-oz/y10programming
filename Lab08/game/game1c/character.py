class Character:

    def __init__(self, name, bio=''):
        self.name = name
        self.bio = bio
        self.conversation = None

    def about(self):
        print(f'👻 {self.name}: {self.bio}')

    def talk(self):
        if self.conversation == '':
            print('I have nothing to say.')
        else:
            print(f'{self.name}: {self.conversation}')


class Player:

    def __init__(self, name, spot, health=10, wealth=10, power=10):
        self.name = name
        self.current_spot = spot
        self.health = health
        self.wealth = wealth
        self.power = power
        self.backpack = {}
        self.awards = {}

    def hud(self):
        print(f'--- 💙:{self.health} 💰:{self.wealth} 🌈:{self.power} ---')

class Enemy(Character):
    def __init__(self, name, bio='', weakness=''):
        super().__init__(name, bio)
        self.weakness = weakness

    def fight(self, weapon):
        if weapon == self.weakness:
            print(f'You fend off {self.name} with the {weapon}.')
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer.')
            return False
