def calculate_floor(string):
    current_floor = 0  
    for i in string:
        if i == 'U':
            current_floor += 1
        elif i == 'D':
            current_floor -= 1
    return current_floor
print('the number of floor is:',calculate_floor('UDDD ')) #-2
print(calculate_floor('UUUU')) #4