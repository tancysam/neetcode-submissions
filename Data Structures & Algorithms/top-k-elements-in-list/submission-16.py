class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # obtain count of each of the numbers present in the list

        count = {}

        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
        print(count)
        # for each number, place in a bucket frequency
        
        frequency = [[] for _ in range(len(nums))]
        print(frequency)
        for num in count.keys():

            print(count[num]-1)
            frequency[count[num]-1].append(num)
            print(frequency)

        

        # iterate through the buckets from the least to most until len(result) becomes == k

        result = []
        progress = len(frequency) -1
        while not len(result) == k:
            if len(frequency[progress]) > 0:
                for num in frequency[progress]:
                    result.append(num)
            progress -= 1

        return result   
