print('Welcome to Skype log in! Enter 9999 to quit.')
name = input('Enter your name: ')

while name != '9999':
    if name == 'David':
        print('Welcome to Skynet!')
    elif name == 'Jeremy':
        print('On your command, my true master.')
    else:
        print('Self destruction activated... You have 60 seconds to run.')
    name = input('Enter your name: ')
