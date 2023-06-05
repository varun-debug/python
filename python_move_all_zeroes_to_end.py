A = [0,1,0,3,1,2]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j] 
        j += 1
print(A)
