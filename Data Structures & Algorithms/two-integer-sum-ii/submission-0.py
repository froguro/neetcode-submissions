class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        input: array of INT, sorted in non-decreasing order
        output: 1-indexed indices, s.t. they add up to target
        - constraint: index1 + index2 = target, index1 < index2
        - always one valid solution

        brute force: O(n^2) check every number
        better way: keep track of seen numbers? but we want to keep space O(1)
        - make use of nondecreasing property
        - left and right pointer
        [2,4,5,6,8] target = 9
        """ 

        l, r = 0, len(numbers) - 1

        while l < r:
            left_diff = target - numbers[l]
            while left_diff < numbers[r]:
                r -= 1
            right_diff = target - numbers[r]
            while right_diff > numbers[l]:
                l += 1
            if numbers[l] + numbers[r] == target:
                break



        return [l + 1, r + 1]

