class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        how to achieve O(log(mn)) time
        logm + logn
        """

        m = len(matrix)
        n = len(matrix[0])

        # determine which row it is
        # we know that the first value of each row is greater than the last integer of the prev
        # which means that its greater than the first value of the previous

        lo, hi = 0, m - 1

        while lo <= hi: # once lo == hi, then that is the row that should have target
            mid = (lo + hi) // 2
            if target > matrix[mid][-1]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                break

        if not (lo <= hi):
            return False
    
        row = (lo + hi) // 2
        

        print(row)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            elem = matrix[row][mid]
            if elem > target:
                hi = mid - 1
            elif elem < target:
                lo = mid + 1
            else:
                return True
        
        return False
        
