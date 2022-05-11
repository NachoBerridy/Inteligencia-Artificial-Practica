list = [[1,2,3,4]]
list1 = []
list1 = list[:]

for i in list:
    list1.append(i)

list[0].append(18)
print(list1)