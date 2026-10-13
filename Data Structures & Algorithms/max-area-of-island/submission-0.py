class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxArea = 0

        def searchIslands(x,y):
            
            if grid[y][x] == 0 or (x,y) in visited:
                return 0

            visited.add((x,y))

            for (xChange, yChange) in directions:
                if 0 <= (y+yChange) <= len(grid)-1 and 0 <= (x+xChange) <= len(grid[0])-1:
                    v = searchIslands(x+xChange,y+yChange)

            if grid[y][x] == 1:
                nonlocal area
                area += 1
            
            return
                

            
        for y in range(0,len(grid)):
            for x in range(0, len(grid[0])):
                area = 0
                res = searchIslands(x,y)
                maxArea = max(maxArea, area)

        return maxArea
            