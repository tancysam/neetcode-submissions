class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        foundWord = False

        def search(x,y,i:int,visited:set):
            
            if (x,y) in visited or i >= len(word):
                return
             
            
            if board[y][x] == word[i] and i == len(word)-1:
                nonlocal foundWord
                foundWord = True

            
            visited.add((x,y))

            if board[y][x] == word[i]:
                for xChange,yChange in directions:
                    if 0<= (x+xChange) < len(board[0]) and 0<=(y+yChange)<len(board) and i < len(word):           
                        search(x+xChange,y+yChange,i+1,visited)
            visited.remove((x,y))
         
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                visited = set()
                search(x,y,0,visited)
        
        if foundWord == True:
            return True
        return False




            
            