print("Welcome to Jeremy's Super Number Sort")
print("Please enter your numbers on prompt and 'enter only' (empty) to quit.")
# we assume we don't need to handle exceptions to make the code simple.

user_input = 'start'
nlist = []

while True:
    user_input = input("Enter a number: ")
    if user_input == '':
        break
    elif '.' in user_input:
        nlist.append(float(user_input))
    else:
        nlist.append(int(user_input))

print('Your sorted list is: ', sorted(nlist))
