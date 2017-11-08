student_raw = '''
Adam
Bob
Jordan
Tom
Edward
Alex
David
Alistar
JoshA
Yin
Keanu
JoshB
Liam
Jesse
Mike
Aaron
Nick
Daniel
'''

num = 3 # number of assessees per assessor

student_list = [s for s in student_raw.splitlines() if s != '']

shuffle(student_list)
assessors = student_list
assignment = defaultdict(list)
print(assessors)

for i, assessor in enumerate(assessors):
    if (i+1+num) < len(assessors):
        assignment[assessor] = assessors[i+1: i+1+num]
    else:
        assignment[assessor] = assessors[i+1: len(assessors)] + assessors[0: (i+1+num)%len(assessors)]

pprint(assignment)