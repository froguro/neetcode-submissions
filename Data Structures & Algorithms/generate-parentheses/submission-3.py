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
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k-i-1]:
                        dp[k].append("(" + left + ")" + right)
        
        return dp[-1]

