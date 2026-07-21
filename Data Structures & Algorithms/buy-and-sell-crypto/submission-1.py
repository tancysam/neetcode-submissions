class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        minP = 101
        maxProf = 0

        for i in range(0,len(prices)):
            
            if prices[i]<minP:
                minP = prices[i]
            
            maxProf = max(maxProf, prices[i]-minP)

        
       


        return maxProf