# expence =[2200,2350,2600,2130,2190]

# print(expence[1]-expence[0])
# print(expence[0]+expence[1]+expence[2])
# for i in expence:
#     if i==2000:
#        print('yes')
#        break
# else:
#     print('no')
# print(2000 in expence)
# expence.insert(5,1980)
# print(expence)

# expence[3]=1990
# print(expence)

# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))
# heros.append('black panter')
# print(heros)
# heros.remove('black panter')
# heros.insert(3,'black panter')
# print(heros)
# heros[1:3]=['doctor']
# print(heros)

# heros.sort()
# print(heros)
max_number=int(input("enter a number:"))
odd_number=[]
for i in range(1,max_number) :
    if i % 2 ==1 :
        odd_number.append(i)
print(odd_number)