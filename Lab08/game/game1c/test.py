from character import Enemy

dave = Enemy('Dave', 'A smelly zombie.', 'garlic')
dave.conversation = 'I like to eat humans.'
print(dave.bio)
print(dave.chat)
weapon = input('Fight with: ')
dave.fight(weapon)