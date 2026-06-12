class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def rotten(r,c):
            if(r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                grid[r][c] == 0):
                return
            q.append([r,c])
            visited.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 2):
                    q.append([r,c])
                    visited.add((r,c))

        minutes = 0
        if(q):
            minutes -= 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                rotten(r-1,c)
                rotten(r+1,c)
                rotten(r,c-1)
                rotten(r,c+1)
            minutes += 1
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1):
                    return -1
        return minutes


