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
