class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        res = []

        def dfs(x,y,prevHeight):
            
            #Check that we are beyond boundaries
            #pacific check
            #atlantic check
            #check if currHeight is less than prevHeight
            #search 4 directions; check if spot is valid, valid is inclusive of edges

            if (x,y) in visited:
                return

            if x < 0 or x >= len(heights[0]) or y < 0 or y >= len(heights):
                #beyond boundaries

                if x<0 or y < 0:
                    nonlocal pacific
                    pacific = True
                if x>= len(heights[0]) or y>= len(heights):
                    nonlocal atlantic
                    atlantic = True
                return
            else:
                if heights[y][x] <= prevHeight:
                    visited.add((x,y))
                    for xC,yC in directions:
                        dfs(x+xC,y+yC,heights[y][x])
            return
        
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                atlantic = False
                pacific = False
                visited = set()
                dfs(x,y,heights[y][x])

                if atlantic and pacific:
                    res.append([y,x])
        
        return res

        


            