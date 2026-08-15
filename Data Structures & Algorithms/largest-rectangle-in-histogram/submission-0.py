class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            if i == 0:
                stack.append((i, height))
            idx = i
            while stack and height < stack[-1][1]:
                idx, oldHeight = stack.pop()
                maxArea = max(oldHeight * (i - idx), maxArea)
            stack.append((idx, height))
        for i, height in stack:
            maxArea = max(height * (len(heights) - i), maxArea)

        return maxArea
