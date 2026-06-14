class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        #Running dfs to go from pacific to atlantic or atlantic to pacific, only looking at the permiter
        # Go from increasing level as need to flow out instead of decreasing which would require
        # the logic to look  in the middle. The smallest values should be on the edges
        def dfs(r,c,visit,prevH):
            if(r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visit or
                heights[r][c] < prevH):
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])

        #Running through all the first and last rows of the grid
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        #Running throught the first and last column of the grid
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        res = []

        #Getting the intersection of the two sets
        for r in range(ROWS):
            for c in range(COLS):
                if((r,c) in pac and (r,c) in atl):
                    res.append([r,c])
        return res
        
        # res = []

        # def dfs(r,c):
        #     if(r not in range(ROWS) or
        #     c not in range(COLS))

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if(dfs([r,c])):
        #             res.append(r,c)
        
        # return res