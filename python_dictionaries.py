#Acts like a map data structure
dict1={}
print(type(dict1))
dict2={}
dict2['name']='Varun'
dict2['age']= 24
dict2['skills']=['python','c#']
dict2['States']=['Maharashtra','Kerala']
print(dict2)
print('Lenght:',len(dict2))
dict3={'color':'Black','country':'India'}
dict2['other_details']=dict3
print(dict2)
print(' New Lenght:',len(dict2))

#how to access key
print(dict2['name'])
print(dict2['skills'])

#to print the first skill from 2 skils
print(dict2['skills'][0])
#to know the country
print(dict2['other_details']['country'])

#how to update particular value key
dict2['age']=25
print(dict2['age'])

#how to get the keys in dictionary
print(dict2.keys())
#just to print keys
print('Total keys:',list(dict2.keys()))
#how to get the values in dictionary
print(dict2.values())
print(list(dict2.values()))

#how to iterate in dictionary
for k,v in dict2.items():
    print('key is:',k,'and value is:',v)

#compare dictionaries

#here all key and values are same but sequence is changed
dict3={'a':1,'b':2,'c':3,'d':4}
dict4={'b':2,'d':4,'c':3,'a':1}

print(dict3==dict4)

#here the values of one key is changed
dict3={'a':1,'b':2,'c':3,'d':4}
dict4={'b':2,'d':4,'c':3,'a':5}

print(dict3==dict4)

#how to delete specific key value in dictionary
print(dict2)
del dict2['age']
print("After deletion")
print(dict2)

#how to check if key exists in dict or not
print(dict2.keys())
#how to get the values of particular key
print(dict2.get('skills'))
