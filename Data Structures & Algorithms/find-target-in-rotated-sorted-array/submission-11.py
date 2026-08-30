class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
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

        while l <= r:
            mid = (l + r) // 2
            print(nums[l: r + 1])
            if nums[mid] == target:
                return mid
            # Determine which half is sorted
            if nums[mid] > nums[r]:
                # Left half is sorted, right half is rotated
                if nums[l] <= target < nums[mid]:
                    # Target is in sorted left half
                    r = mid - 1
                else:
                    # Target is in rotated right half
                    l = mid + 1
            else:
                # Right half is sorted, left half is rotated
                if nums[mid] < target <= nums[r]:
                    # Target is in sorted right half
                    l = mid + 1
                else:
                    # Target is in rotated left half
                    r = mid - 1
        
        return -1