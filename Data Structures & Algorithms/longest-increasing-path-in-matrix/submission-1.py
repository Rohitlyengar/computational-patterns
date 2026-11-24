class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def DFS(r: int, c: int, curr: int, prev: int):
            nonlocal res
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return

            res = max(res, curr)

            DFS(r + 1, c, curr + 1, matrix[r][c])
            DFS(r - 1, c, curr + 1, matrix[r][c])
            DFS(r, c + 1, curr + 1, matrix[r][c])
            DFS(r, c - 1, curr + 1, matrix[r][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                DFS(r, c, 1, float('-inf'))
        return res

