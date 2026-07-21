class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = 0
        for i in prices:
            if i < buy:
                buy = i
                sell = 0
            sell = max(i, sell)
            profit = max(profit, sell - buy)
        return profit

        