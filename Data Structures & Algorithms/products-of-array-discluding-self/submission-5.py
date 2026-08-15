class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # [1,2,4,6]
        pre = [1 for _ in range(n)]
        # [1, 1, 2, 8] the product of all before it
        post = [1 for _ in range(n)]
        # [48, 24, 6, 1] the product of all after it
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        res = []
        for i in range(n):
            res.append(post[i] * pre[i])
        return res



