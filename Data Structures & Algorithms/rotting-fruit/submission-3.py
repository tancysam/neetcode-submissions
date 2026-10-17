class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        
        # Queue all rotten fruits in grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    queue.append((x,y))
        
        # BFS 
        '''
        For each rotten fruit in queue, 
        Check if they have fresh fruits surrounding them. Then mutate in place to indicate they are rotten.
        Repeat until queue is empty
        '''

        currLvl = -1
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while queue:
            currLvl += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                
                for xChange,yChange in directions:
                    if 0 <= x+xChange < len(grid[0]) and 0 <= y+yChange < len(grid):
                        if grid[y+yChange][x+xChange] == 1:
                            queue.append((x+xChange,y+yChange))
                            grid[y+yChange][x+xChange] = 2

        #Check for fresh fruits still in grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    print((x,y))
                    return -1
        return max(0,currLvl)
                    

                

                

            
