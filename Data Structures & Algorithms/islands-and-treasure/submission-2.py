class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # adds the children starting from each treasure
        def addIsland(r,c):
            if(r not in range(ROWS) or c not in range(COLS)
                or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])

        #Getting all the starting positions of the gates
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 0):
                    q.append([r,c])
                    visited.add((r,c))
        # runs bfs as the first time an island is reached it will be marked as visited an therefore not updated
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist

                addIsland(row+1,col)
                addIsland(row-1,col)
                addIsland(row,col-1)
                addIsland(row,col+1)
            dist += 1
        # rows, cols = len(grid), len(grid[0])
        # def dfs(r,c,visited):
        #     if(r not in range(rows) or
        #         c not in range(cols) or
        #         grid[r][c] == -1 or
        #         (r,c) in visited):
        #         return float("inf")
        #     if(grid[r][c] == 0):
        #         return 0
        #     visited.add((r,c))
        #     return min(1+dfs(r+1,c,visited),
        #         1+dfs(r-1,c,visited),
        #         1+dfs(r,c-1,visited),
        #         1+dfs(r,c+1,visited))

        # for r in range(rows):
        #     for c in range(cols):
        #         if(grid[r][c] == 2147483647):
        #             grid[r][c] = dfs(r,c,set())
        