# a=10
# print(a/0)
#ZeroDivisionError: division by zero
# print('Hello')

# list_a=[5,3,1,6,7]
# print(list_a[7])
#IndexError: list index out of range

a=5
try:
    print(a/0)
#if some error comes than the control will be transfered to except block
#it will not hold the prb to exceutev 
except:
    print('Some error has occured')

print('Bye!!!!')

num=5
list_a=[1,2,3,4,5]
dict_b={'Varun':20,'AKshay':40}

try:
    result = num/5
    print(result)

    print(list_a[2])
    print(dict_b['abcd'])

#only one error can be displayed at a time 
except ZeroDivisionError:
    print('Error occured because zero division has occured')
except IndexError:
    print('Because index error has occured')
except KeyError:
    print("Key was not there in the dictionary")

#or else u can directly give one stmt to show exception
except Exception as err:
    print("Error occured:",err)
 
a=5
try:

    result = a/0
    print(result)
except ZeroDivisionError:
    print('Divide by zero')

#if try is successfull with no error than else will get execute
else:
    print('calculate the result')
    print(result)

#doesn't matter of success and fail of try this will exceute no matter whats happens
#it can be used to release the resources
finally:
    print("I will get execute doesn't matter what comes ")
