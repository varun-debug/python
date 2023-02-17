#write a prg to generate list of 10 no.
list1=[]
for i in range(1,11):
    list1.append(i)

print(list1)

#how to do it with the help of list comprehension
list1=[i for i in range(1,12)]
print(list1)

#convert all string into uppercase
list_a=['abc','upper','varun','akshay','vaibhav']
uppercase_result = [ i.upper() for i in list_a]
print(uppercase_result)

#put all negative no.after postive no. in the list
list_x=[-1,2,-6,9,-4,7]
positive_result=[x for x in list_x if x>0 ]
positive_result1=[x for x in list_x if x<0 ]
print(positive_result + positive_result1)
#o/p [2, 9, 7, -1, -6, -4]
