class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        trackFreq = {}

        for num in nums:
            trackFreq.setdefault(num,0)
            trackFreq[num] += 1
        
        freq = [None] * len(nums)

        for key,value in trackFreq.items():
            freq[value-1] = key
        
        mostFreq = []
        count = len(freq)-1

        while len(mostFreq) < k:
            if freq[count]:
                mostFreq.append(freq[count])
            count -= 1
        
        return mostFreq


            