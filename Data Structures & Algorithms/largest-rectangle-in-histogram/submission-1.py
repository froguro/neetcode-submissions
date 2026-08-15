class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        """
        one pass solution:
        1. if height[i] is greater than the height at the top of the stack
        push to the stack.
        2. if its less, then pop from the stack and calculate the area of the popped rectangle
        the intuition is that we can't extend that rectangle any longer
        -> the new appended item would be pushed into the stack with the same index asthe popped item
        -> the intuition here is that since the current height is less than the popped one, it 
        can be extended all the way left to where the popped index was
        """
        for i, height in enumerate(heights):
            idx = i
            while stack and height < stack[-1][1]:
                idx, oldHeight = stack.pop()
                maxArea = max(oldHeight * (i - idx), maxArea)
            stack.append((idx, height))
        # for the remaining items in the stack, calculate their potential areas
        for i, height in stack:
            maxArea = max(height * (len(heights) - i), maxArea)

        return maxArea
