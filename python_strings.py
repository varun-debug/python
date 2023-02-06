str1="Varun"
str2='Genius'
print(str1)
print(str2)
print('length of string:',len(str1))
str3='''hello 
how r u
I am good'''
print(str3)
#string concat
print(str1 + str2)
#string comparision
print(str1 == str2)

for i in str1:
    print(i)

#update the specific character in string not possible because it is immutable
# str1[1]="x"
# print(str1) 

#lower and upper
print('Lower: ',str1.lower())
print('Upper: ',str1.upper())
