class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                square = ((row // 3),(col // 3))
                if val == '.':
                    continue
                elif val not in rowSet[row] and val not in colSet[col] and val not in squareSet[square]:
                    squareSet[square].add(val)
                    rowSet[row].add(val)
                    colSet[col].add(val)
                else:
                    return False
        return True
