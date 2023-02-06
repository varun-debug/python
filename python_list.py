L1 = []
print(type(L1))
# L1.append(1)
# L1.append(2)
# L1.append(3)
# L1.append(4)

#u can insert multiple values using loop
for num in range(1,11):
    L1.append(num)
print(L1)

#length of list
print("Lenght of list:",len(L1))

#to check both list are equal
list1=[1,"Varun",20,"Hi"]
list2=[1,"Varun",20,"Hi"]

print("List are equal? ",list1==list2)

list1=[1,"Varun",20,"Hi"]
list2=[1,"Varun",20,"hi"] #just changed captilal H to h so for equal sequence+same orientation should match
print("List are equal? ",list1==list2)

list3=[1,2,3,4,5]
list4=[10,20,30,40,50]
result=list3 + list4 #concatination
print(result)

#how to access the elements in the list
list6=[20,30,40,50,60]

#print all the elements in the list Opt 1
for i in list6:
    print(i)

#print the particular element in the list opt 2
print("1st element:",list6[0])
print("2nd element:",list6[1])

#what will happen if index is more then elements
#will throw error list index out of range
#print("100th element:",list6[100])
#how to update the value of list index
print("-----------------------------------")
L1=[1,'Akshay',20]
print(L1)
L1[1]="Varun"
print("After update: ",L1)

#How to print list elemetns using lenght
# for index in range(0,len(L1)):
#     print(L1[index])

#difference between append() and extend
list5=[1,2,5,"Varun",[5,5,5],"Vishal"]
print("Length before append:",len(list5))
list5.append([20,30])
print(list5)
print("Length after append:",len(list5))
list5.extend([200,"vikas",300])
print(list5)
print("Length after extend:",len(list5)) #in short append to add single element and extend to add multiple elements

#List slicing
list10=[0,1,2,4,7]
print(list10[0:3])
print(list10[0:])
print(list10[0:5:2])#to jump by 2 places 
print(list10[-1::-1])
