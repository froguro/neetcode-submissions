class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1) # where dp[i] is the number of ways to climb i stairs
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            # [1, 1, 2, 3]
        
        return dp[n]