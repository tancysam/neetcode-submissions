class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minP = float('inf')
        maxProf = 0

        for price in prices:

            if price < minP:
                minP = price
            tmp = price - minP
            maxProf = max(maxProf, tmp)

        return maxProf