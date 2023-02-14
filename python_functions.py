# #functions in python
# #eg len() to calculate the length 
# #inbuilt functions eg. there are many more u can go through the python documentation
# list1=[1,2,3,4,5,6]
# print('Max no:',max(list1))
# print('Min no:',min(list1))
# print('Sum:',sum(list1))

# #user defined one
# def sum_of_two(a,b):
#     c=a+b
#     return c
# print(sum_of_two(5, 5))

# def msg_bot():
#     print('Welcome')
# msg_bot()

#fun to find the avg of two no
def avg_two_no(a,b):
    avg_result=(a+b)/2 #do not want decimals we can use '//'
    return avg_result
print(avg_two_no(10,5))

#fun to calculate factorial

# def fact(no):
#     sum=1
#     if no== 0 or no==1:
#         return 1
#     while no>1:
#         sum *= no
#         no -=1 
#     return sum
# print(fact(1))

#using for loop
# def factorial(n):
#     if n== 0 or n==1:
#         return 1
#     sum=1
#     for num in range(1,n+1):
#         sum *=num
#     return sum

# print(factorial(5))

#multiple assigning the variables 
a,b,c=1,2,3
print(a,b,c)
def square_and_cube(n):
    square = n*n
    cube = n*n*n
    return square,cube
print("Square and cube of no:",square_and_cube(5))

#how to create optional arguments in python
def multiple(a,b=3):
    result=a*b
    return result
print("Overwrite the value:",multiple(5,10))
print("Optinal:",multiple(5))

#non-key valued arguments 
def eg_non_key_value(*arg):
    for param in arg:
        print(param)

eg_non_key_value('Welcome','To','My','World')

#key value type of arguments in python
def eg_key_value(**karg):
    for k,v in karg.items():
        print('Key is ',k,'and Value is ',v)

eg_key_value(Name='Varun', age=24, Domain='Data Engineer')
