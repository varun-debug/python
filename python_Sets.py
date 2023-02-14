set1=set()
print(type(set1))

#it does not take duplicate values
list1=[1,2,3,4,1,5,2,3,6,4]
set2=set(list1)
print(set2)

set3={1,2,3,4,1,5,2,3,6,4}
print(set3)
print(type(set3))

#so be careful to create empty set because if values are not there than it works as dictionary
set4={}
print(type(set4))

#iterate
for num in set3:
    print(num)

#convert output of set into the list
set5=list(set(list1))
print(set5)
print(set5[1])

#how to insert elements in the Set
set6=set()
set6.add(1)
set6.add(2)
set6.add(1)
set6.add(3)
set6.add(5)
print(set6)

#how to update the elements in the set
temp=[1,2,3,2,4,2,6,4,5,1,2,3,6,7]
set6.update(temp)
print(set6)

#calculate the length of the set
print('Length of Set:',len(set6))

#set operations
set_a={1,2,3,4,5,6}
set_b={3,6,8,9,10}

#union operation
#print(set_a.union(set_b)) #or
print(set_a | set_b)

#intersection operation
#print(set_a.intersection(set_b))
print(set_a & set_b)

#A-B ?
#B-A ?
#difference
#print(set_a.difference(set_b)) or
print(set_a - set_b)
#print(set_b.difference(set_a)) or
print(set_b - set_a)

#comparison in Sets
set_x={1,2,3,4,5,6}
set_y={1,2,3,4,5,6,2,3,1}
#true because it eleminates duplicate
print(set_x == set_y)

set_x={1,2,3,4,5,6}
set_y={1,2,3,4,5,6,2,3,1,7}
print(set_x == set_y)
