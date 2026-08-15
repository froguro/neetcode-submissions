class Solution:
    def trap(self, height: List[int]) -> int:
        """
        height of water in an area: min(height[r], height[l]) * (r - l) - (the heights of the inbetween...)
        """
        n = len(height)

        prefix = [0] * n
        suffix = [0] * n

        # store prefix and suffix maximums for each position
        prefix[0] = height[0]
        suffix[n - 1] = height[n - 1]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            
            suffix[i] = max(suffix[i + 1], height[i])

        # iterate through the array with index i and calc the total water
        res = 0
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]

        return res