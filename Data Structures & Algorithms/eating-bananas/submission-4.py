class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = float('+inf')
        while l <= r:
            m = (r + l) // 2
            temp = 0
            for num in piles:
                temp += math.ceil(num/m)
            
            if temp <= h:
                k = min(k,m)

            if temp <= h:
                r = m-1
            else:
                l = m+1

        return k