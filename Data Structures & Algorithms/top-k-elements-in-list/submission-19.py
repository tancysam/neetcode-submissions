class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        trackFreq = {}

        for num in nums:
            trackFreq.setdefault(num,0)
            trackFreq[num] += 1
        
        freq = [[] for num in range(len(nums)+1)]

        for key,value in trackFreq.items():
            freq[value].append(key)
        
        res = []
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if len(res)<k:
                    res.append(num)

        return res


        


            