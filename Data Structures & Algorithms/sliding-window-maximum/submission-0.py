class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        """
        nlogn time??
        n -> linear search
        nlogn -> linear search, with binary search at each step?

        what do we know:
        at each step:
        - the previous k - 1 elements in the window
        - the maximum of the previous


        example:
        [1,2,1,0,4,2,6] 
        [0,1,1,2,2,4,6] <- what if we sorted, and popped the 
        """

        l, r = 0, k - 1
        res = []
        while r < len(nums):
            print(l, r)
            res.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return res

