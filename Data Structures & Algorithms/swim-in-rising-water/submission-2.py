class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = []
        N = len(grid)
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        heapq.heappush(heap,[grid[0][0],0,0])
        visited.add((0,0))

        while heap:
            h, r, c = heapq.heappop(heap)
            if(r == N-1 and c == N-1):
                return h
            
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if(row not in range(N) or col not in range(N) or (row,col) in visited):
                    continue
                heapq.heappush(heap,[max(h,grid[row][col]),row,col])
                visited.add((row,col))
    
        