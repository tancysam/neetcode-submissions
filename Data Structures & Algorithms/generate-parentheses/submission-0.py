class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(string, opened, closed):
            
            if len(string) == 2*n:
                if opened == closed:
                    res.append(string)
                return
            
            if closed > opened:
                return

            backtrack(string + '(', opened+1, closed)
            backtrack(string + ')', opened, closed+1)

            
        backtrack('',0,0)
        return res
            


            
            

