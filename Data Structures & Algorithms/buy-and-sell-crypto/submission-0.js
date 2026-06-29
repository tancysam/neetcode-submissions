class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let b = 0
        let s = 1
        let maxP = 0

        for (s=0; s<prices.length; s++){
            if (prices[b] > prices[s]){
                b = s
            } else {
                let profit = prices[s] - prices[b]
                maxP = Math.max(maxP, profit)
            }
        }

        return maxP

    }
}
