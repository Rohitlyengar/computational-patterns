class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addCell(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r, c) in visit:
                return
            q.append([r, c])
            visit.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1:
                    grid[r][c] = 3

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            res += 1
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max(0, res - 1)
