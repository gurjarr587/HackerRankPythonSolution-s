def binomial(n,k):
    C = [[0 for i in range(k+1)]for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                C[i][j] = 1

            else:
                C[i][j] = C[i-1][j-1]+C[i-1][j]
    return C[n][k]
n=5
k=2
binomial(n,k)
print("Value of C["+str(n)+"]["+str(k)+"]is "+str(binomial(n,k)))