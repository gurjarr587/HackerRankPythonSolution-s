
'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0 
'''

###########################CODE START################################

maximum = 0
# Complete the hourglassSum function below.
def hourglassSum(A):
    global maximum

    for row in range(len(A)-2):

        for column in range(len(A[row])-2):
            t1 = A[row][column]
            t2 = A[row][column+1]
            t3 = A[row][column+2]

            m1 = A[row+1][column+1]

            l1 = A[row+2][column]
            l2 = A[row+2][column+1]
            l3 = A[row+2][column+2]
            sum = t1+t2+t3+m1+l1+l2+l3

            if(maximum<sum):
                maximum = sum
    print(maximum)


if __name__ == '__main__':
    A = []
    in_x = int(input("insert: "))
    in_y = int(input("insert: "))

    for x in range(in_x):
        A.append([])
        for y in range(in_y):
            A[x].append(int(input()))
    print(A)
    result = hourglassSum(A)

###########################CODE ENDS################################


OUTPUT:
insert: 3
insert: 4
1
2
3
4
5
6
7
1
2
3
4
5
[[1, 2, 3, 4], [5, 6, 7, 1], [2, 3, 4, 5]]
28

Process finished with exit code 0
