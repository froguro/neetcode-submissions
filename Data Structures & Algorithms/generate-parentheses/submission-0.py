class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        input: n - int
        output: list of strings: well-formed parentheses that you can generate n pairs of parentheses. all the
        ways you can form n valid pairs of parentheses
        constraints: 1 <= n <= 7


        we need 2n parentheses

        base case: 2n parenthesis 
        1 opening parenthesis: can have another opening, or closing
        2 open, 0 close: can have another opening, or closing
        -> if 0 closing and nonzero open: can have closing or open
        -> if 0 opening: can only have open
        -> if close < open: can have a close
        """
        
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n: # you cannot have more opening paren than n 
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN: # you cannot have more closing parent than open
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res

