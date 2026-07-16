class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        N = len(grid)
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        heap = []
        heapq.heappush(heap,[grid[0][0],0,0])
        visited.add((0,0))

        while heap:
            h, row, col = heapq.heappop(heap)
            if(row == N-1 and col == N-1):
                return h
            
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if(r not in range(N) or c not in range(N) or (r,c) in visited):
                    continue
                heapq.heappush(heap,[max(h,grid[r][c]),r,c])
                visited.add((r,c))

        # visited = set()
        # directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # ROW, COL = len(grid), len(grid[0])

        # q = deque()
        # q.append([0,0])
        # time = 0
        # while q:
        #     print(grid)
        #     for i in range(len(q)):
        #         row, col = q.popleft()
        #         while(grid[row][col] != 0):
        #             time += 1
        #             q.append([row,col])
        #             row,col = q.popleft()
        #         visited.add(tuple([row,col]))
        #         if(row == ROW-1 and col == COL-1):
        #             return time
        #         for r,c in directions:
        #             point = [row+r,col+c]
        #             if(row+r in range(ROW) and
        #             col+c in range(COL) and
        #             tuple(point) not in visited):
        #                 q.append(point)
        #     for i in range(ROW):
        #         for j in range(COL):
        #             if(grid[i][j]-time <= 0):
        #                 grid[i][j] = 0
        
        # return time