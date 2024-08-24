"""

Intuition:
    This is similar to unbounded knapsack.
    Similarity:
        price of each piece is like weights
        n(no. of pieces) is N (W)
        We need to create a cuts[] which indicates the length of pieces /val

        A rod of length N can be divided into any numb of pieces such that total is ==N.

"""

 #User function Template for python3
#MEMOIZATION
class Solution:
    def cutRodUtil(self,index,N,price,cuts,dp):
        if index==0:
            if cuts[index]<=N:
                return N//cuts[index]*price[index]
            return 0

        if dp[index][N] != -1:
            return dp[index][N]

        notPick = 0 + self.cutRodUtil(index-1,N,price,cuts,dp)
        pick = notPick
        if cuts[index]<=N:
            pick = price[index]+self.cutRodUtil(index,N-cuts[index],price,cuts,dp)
        dp[index][N] =  max(pick,notPick)
        return dp[index][N]


    def cutRod(self, price, n):
        if n==1:
            return price[0]
        if n==0:
            return 0
        #code here
        cuts = [i+1 for i,j in enumerate(range(n))]
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.cutRodUtil(n-1,n,price,cuts,dp)

#Tabulation
def cutRod(self, price, n):
        if n==1:
            return price[0]
        if n==0:
            return 0
        #code here
        cuts = [i+1 for i,j in enumerate(range(n))]
        dp = [[0 for _ in range(n+1)] for _ in range(n)]

        for i in range(cuts[0],n+1):
            dp[0][i] = (i//cuts[0]) * price[0] #total price i can get when I have to use 'i' cuts[0]

        for i in range(1,n):
            for j in range(1,n+1):
                notPick = dp[i-1][j]
                pick = notPick
                if cuts[i]<=j:
                    pick = price[i]+dp[i][j-cuts[i]]
                dp[i][j] = max(pick,notPick)

        return dp[n-1][n]

#SpaceOptimized
def cutRod(self, price, n):
    if n==1:
        return price[0]
    if n==0:
        return 0
    #code here
    cuts = [i+1 for i,j in enumerate(range(n))]
    #dp = [[0 for _ in range(n+1)] for _ in range(n)]
    prev = [0]*(n+1)

    for i in range(cuts[0],n+1):
        prev[i] = (i//cuts[0]) * price[0] #total price i can get when I have to use 'i' cuts[0]

    for i in range(1,n):
        curr = [0]*(n+1)
        for j in range(1,n+1):
            notPick = prev[j]
            pick = notPick
            if cuts[i]<=j:
                pick = price[i]+curr[j-cuts[i]]
            curr[j] = max(pick,notPick)
        prev = curr

    return prev[n]

#1D Space Optimized: Since we are needing only the value from previous row of same column,
# we can maintain the values in same array
# Ex: Lets say We have to calculate the cur[3] element, we need only a single variable (preValue). The catch is that we can initially place this preValue at the position cur[3] (before finding its updated value) and later while calculating for the current row’s cell cur[3], the value present there automatically serves as the preValue and we can use it to find the required cur[3] value. ( If there is any confusion please see the code).
# After calculating the cur[3] value we store it at the cur[3] position so this cur[3] will automatically serve as preValue for the next row. In this way, we space-optimize the tabulation approach by just using one row.
def cutRod(self, price, n):
    if n==1:
        return price[0]
    if n==0:
        return 0
    #code here
    cuts = [i+1 for i,j in enumerate(range(n))]
    #dp = [[0 for _ in range(n+1)] for _ in range(n)]
    dp = [0]*(n+1)

    for i in range(cuts[0],n+1):
        dp[i] = (i//cuts[0]) * price[0] #total price i can get when I have to use 'i' cuts[0]

    for i in range(1,n):
        for j in range(1,n+1):
            notPick = dp[j]
            pick = notPick
            if cuts[i]<=j:
                pick = price[i]+dp[j-cuts[i]]
            dp[j] = max(pick,notPick)

    return dp[n]
