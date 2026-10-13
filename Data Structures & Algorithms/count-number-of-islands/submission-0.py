class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0

        def searchIslands(x,y):
            
            
            if grid[y][x] == '0' or (x,y) in visited:
                return 0

            visited.add((x,y))
            v=0
            for (xChange, yChange) in directions:
                if 0 <= (y+yChange) <= len(grid)-1 and 0 <= (x+xChange) <= len(grid[0])-1:
                    v = searchIslands(x+xChange,y+yChange)

            if v == 1 or grid[y][x] == '1':
                return 1
            else:
                return 0

            
        for y in range(0,len(grid)):
            for x in range(0, len(grid[0])):
                res = searchIslands(x,y)
                if res == 1:
                    print(x,y)
                    islands += 1

        return islands
            
                


