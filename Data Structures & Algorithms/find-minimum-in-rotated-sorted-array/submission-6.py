class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        finding the "left sorted half" and the "right sorted half"
        once we calculate the mid index, determine which half you are currently in

        1 2 3 4 5 6
        6 1 2 3 4 5
        5 6 1 2 3 4
        4 5 6 1 2 3
        3 4 5 6 1 2
        2 3 4 5 6 1
        1 2 3 4 5 6

        """

        l = 0
        r = len(nums) - 1

        while l < r:
            midIdx = (l + r) // 2
            mid = nums[midIdx]
            left = nums[l]
            right = nums[r]
            if mid > right:
                l = midIdx + 1
            else:
                r = midIdx
        

        return nums[l]