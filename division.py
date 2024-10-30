selected_number = int(input('please enter an integer: '))
for x in range(selected_number):
    if(x % 3 == 0 and x % 5 == 0):
        print(x)
