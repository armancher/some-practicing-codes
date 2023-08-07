import random
rolling_dice='y'
min_value=1
max_value =6
while rolling_dice =='y':
    print("dice is rolling ")
    value1=random.randint(min_value,max_value)
    value2=random.randint(min_value,max_value)
    print(value1,value2)
    rolling_dice=input("roll again press 'y'")
 
 