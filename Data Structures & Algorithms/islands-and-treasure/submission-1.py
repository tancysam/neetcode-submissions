class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        visited = set()
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    queue.append((x,y))

        currLvl = 0
        currLvlAmt = len(queue)

        while queue:
            if currLvlAmt == 0:
                currLvl += 1
                currLvlAmt = len(queue)
            currLvlAmt -= 1

            x,y = queue.popleft()

            if grid[y][x] == -1 or (x,y) in visited:
                pass
            else:
                for xChange,yChange in directions:
                    if 0 <= x+xChange < len(grid[0]) and 0 <= y+yChange < len(grid):
                        queue.append((x+xChange,y+yChange))

                visited.add((x,y))
                grid[y][x] = currLvl
            
            
        
            
            
        
        

        


            
            



