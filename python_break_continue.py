int_list = [1,3,6,7,9,13,2]

#break keyword example
for i in int_list:
    print("Current num=",i)
    if(i % 2 == 0):
        print("Even Num=",i)
        break

#continue keywork example
for i in range(1,21):
    if(i<10):
        continue #it will just move fwd by neglecting the no. les then 10
    print(i)
