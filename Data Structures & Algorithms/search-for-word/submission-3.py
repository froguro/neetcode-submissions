class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtracking(i, r, c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or word[i] != board[r][c] or board[r][c] == "#":
                return False
            
            board[r][c] = "#"
            res = (backtracking(i + 1, r + 1, c) or 
                    backtracking(i + 1, r - 1, c) or 
                    backtracking(i + 1, r, c + 1) or 
                    backtracking(i + 1, r, c - 1))
            board[r][c] = word[i]
            return res

        for r in range(m):
            for c in range(n):
                if backtracking(0, r, c):
                    return True
        return False

        