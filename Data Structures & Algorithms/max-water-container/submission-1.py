class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        input: array of ints containing heights of each ith bar
        output: integer of maximum area
        max height is determined by min(height1, height2)
        width is determined by right - left index
        """

        res = 0

        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            res = max(height * width, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        