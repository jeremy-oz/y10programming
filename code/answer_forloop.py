import random
import time

students = ['Omar', 'Burak', 'Jordan', 'Tony', 'Tyson', 'Jack',
            'Edwin', 'Alejandro', 'Rick', 'David', 'Ali Akbar',
            'Josh', 'Yahqub', 'Keanu', 'Josh', 'Jarrod', 'Liam',
            'Jesse', 'Moustafa', 'Armaan', 'Navish', 'Daniel']

quizzes = [
('What version of Python do you use?', '3.6'),
('True or False: Python is only free for students.', 'False'),
('What three technologies are needed for web design? HTML5/CSS3/and ...', 'Javascript'),
('If I want to stop my program, which package do I use?', 'time'),
('Python has two kinds of loop, one is "while loop" and the other is ___ loop?', 'for'),
('To shuffle a list of students, which packagedo I use?', 'random'),
('True or False, Python is used to build web servers.', 'True'),
('Which site is not built in Python? YouTube, Instagram, Facebook, Dropbox', 'Facebook'),
("True or False: This is a correct list in Python: [1, 'John', 4.5]", 'True'),
("True or False: print('X' * 10) will print 10 Xs on the screen.", 'True'),
('What is the result of 5 ** 2 in Python?', '25'),
('True or False: To compare a and b, you use "a == b" instead "a = b"', 'True')
]


for name in students:
    time_to_answer = random.randint(1, 10)
    print()
    print(f"{name}, you've got {time_to_answer} seconds to answer this question or detention!")
    quiz, answer = random.choice(quizzes)
    print('\nQuiz: ', quiz)
    print('Start', end='')
    for second in range(time_to_answer):
        print('.', end='', flush=True)
        time.sleep(1)
    print('Stop\nAnswer:', answer, '\n\n' + '=' * 70)
