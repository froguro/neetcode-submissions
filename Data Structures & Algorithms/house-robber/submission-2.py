class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = nums[1]



        for i in range(2, n):
            dp[i] = nums[i] + max(dp[:i-1])
        
        return max(dp[n - 1], dp[n - 2])
