class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if(r not in range(ROWS) or 
                c not in range(COLS) or
                (r,c) in visited or
                grid[r][c] != 1):
                return 0
            visited.add((r,c))
            return (1 + dfs(r-1,c)+
                        dfs(r+1,c)+
                        dfs(r,c-1)+
                        dfs(r,c+1))
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1):
                    area = max(area,dfs(r,c))
        return area

        # BFS
        # if(not grid):
        #     return 0
        
        # ROWS, COLS = len(grid), len(grid[0])
        # res, visited = 0, set()

        # def bfs(r,c):
        #     q = collections.deque()
        #     q.append((r,c))
        #     visited.add((r,c))
        #     res = 0

        #     while(q):
        #         rw, cl = q.popleft()
        #         res += 1
        #         dx = [[1,0],[-1,0],[0,-1],[0,1]]
        #         for rd,cd in dx:
        #             r, c = rw+rd, cl+cd
        #             if(r in range(ROWS) and
        #                 c in range(COLS) and 
        #                 (r,c) not in visited and
        #                 grid[r][c] == 1):
        #                 q.append((r,c))
        #                 visited.add((r,c))
        #     return res

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if(grid[r][c] == 1 and (r,c) not in visited):
        #             area = bfs(r,c)
        #             res = max(res,area)
        # return res