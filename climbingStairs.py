# Takes too much time???
class Solution(object):
    def climbStairs(self,n):
        if(n==1):
            return 1
        if(n==2):
            return 2

        return climbStairs(n-1)+climbStair(n-2)

# Another one but bad time complexity
class Solution(object):
    def climbStairs(self,n):
        total2s=n//2
        ans=0
        if(n%2==1):
            total1s=1
        else:
            total1s=0

        while(total2s>=9):
            ans+=((math.factorial(total2s+total1s))//(math.factorial(total2s)*(math.factorial(total1s))))
            total2s-=1
            total1s+=2

        return ans

# Best solution
class Solution(object):
    def climbStairs(self,n):
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]

