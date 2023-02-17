#how to create lambda functions

#First normal fun to add int 5 in a given no
def add_no(n):
    result=n+5
    return result

print(add_no(5))

#now same fun using lambda
lamda_add_5=lambda x:x+5
print(lamda_add_5(10))

#lambda fun to add two no
lambda_add_two=lambda x,y:x+y
print(lambda_add_two(10,10))

#write a lambda function to concatenate two strings 
lambda_concat_two=lambda str1,str2:str1 +" "+str2
str1="Hello"
str2="Varun"
print(lambda_concat_two(str1,str2))

#write lambda function to calculate max between two no without max
lambda_max_two=lambda x,y: x if x>y else y
print('Max no:',lambda_max_two(5,10))

#implement map function
list1=[1,2,3,4,5,6,7,8,9]

#result[1, 4, 9, 16, 25, 36, 49, 64, 81]
square_no=lambda x : x*x
square_list=list(map(square_no,list1)) #typecast to list to display map 
print(square_list)

#add sequential respective elements in two given lists
#means add first element with other list first element
list_a=[1,2,3,4,5]
list_b=[5,4,3,2,1]
add_two_list=lambda x,y: x + y
sum_two_list=list(map(add_two_list, list_a,list_b))
print(sum_two_list)

#output= [6,6,6,6,6]

#how to reduce 
#we need to import to use reduce functionality

import functools
list_x=[1,2,3,4,5]
add_two_nums=lambda x,y: x + y

result=functools.reduce(add_two_nums,list_x)
print(result)


multiply_two_no=lambda x,y: x * y

result=functools.reduce(multiply_two_no,list_x)
print(result)

#how to use filter
#create filter to see only odd no
seq=[1,2,4,5,7,8,9]

odd_no = lambda x: x%2!=0
result = list(filter(odd_no,seq))
print(result)
