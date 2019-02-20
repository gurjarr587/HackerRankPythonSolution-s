def pairup(n):
    dp = [0 for i in range(n+1)]
    for i in range(n+1):
        if(i<=2):
            dp[i]=i
        else:
            dp[i]=dp[n-1]+(n-1)*dp[n-2]
    return dp[n]
n=4
print(pairup(n))