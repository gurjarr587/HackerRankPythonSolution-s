
a = int(input("no. of elements: "))
d = int(input("no. of rotation: "))
A = []
for i in range(a):
    nd = int(input())
    A.append(nd)

for i in range(d):
    temp = A[0]
    for i in range(a-1):
        A[i] = A[i+1]
    A[a-1] = temp
print(" ".join(map(str,A)))



OUTPUT:
no. of elements: 3
no. of rotation: 3
7
5
9
7 5 9

Process finished with exit code 0
    
    
