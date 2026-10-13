class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        for i in range(1,max(piles)+1):
            temp = 0
            for num in piles:
                temp += math.ceil(num/i)
            
            if temp <= h:
                return i
            


    

        

        