numbers=[3,4,5,6,6,7,8,4,2,0] #6,4
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print("duplicate number is :",numbers[i])
