"""
take input from user
and find out if the number is a prime number
"""
number=int(input("enter a number:"))
print(f'yuor number is :{number}')

for i in range(2,number):
    if number % i ==0:
        print("it is not prime number!")
        break
    else :
        print(f'{number} is a prime number')
        break
      
      