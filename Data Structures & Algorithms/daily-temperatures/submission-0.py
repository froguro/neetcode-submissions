class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        input: list of ints: temperatures[i] represents temperature on the ith day
        output: list of ints: result[i] is the number of days after the ith day before warmer temperature appears. if no day result[i] = 0
        constraints: 1 <= temperatures.length <= 1000
                     1 <= temperatures[i] <= 100
        edge cases:
        """

        res = [0] * len(temperatures)
        stack = [0] # keeps track of the indices, result[i] = stack[-1] - stack[-2]

        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[i - 1]:
                while temperatures[stack[-1]] < temperatures[i]:
                    print(stack[-1])
                    idx = stack.pop()
                    res[idx] = i - idx
                    if not stack:
                        break
            stack.append(i)

        return res
