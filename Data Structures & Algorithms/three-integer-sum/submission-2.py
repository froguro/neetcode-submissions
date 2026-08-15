class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        input: array of INT
        output: array of int arrays
        constraints: return triplets i,j,k s.t. i +j +k = 0

        we can loop with i and j, and calculate k as we go
        k = - i - j = - (i + j)
        """
        res = []
        nums.sort() 

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                target = -nums[i]
                total = nums[j] + nums[k]
                if target > total:
                    j += 1
                elif target < total:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

        return res

                
