student_raw = '''
Omar
Burak
Jordan
Tony
Tyson
Jack
Edwin
Alejandro
Rick
David
Ali Akbar
Josh
Yahqub
Keanu
Josh
Jarrod
Liam
Jesse
Moustafa
Armaan
Navish
Daniel
'''

student_list = [s for s in student_raw.splitlines() if s != '']
print(student_list)
