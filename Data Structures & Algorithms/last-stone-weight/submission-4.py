class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapStone = []
        for stone in stones:
            heapq.heappush(heapStone,-stone)

        while len(heapStone) > 1:
            
            s1 = -heapq.heappop(heapStone)
            s2 = -heapq.heappop(heapStone)

            
            if s1 == s2:
                pass
            else:
                heapq.heappush(heapStone, -abs(s1-s2))
            
        if len(heapStone) == 0:
            return 0
        else:
            return -heapStone[0]