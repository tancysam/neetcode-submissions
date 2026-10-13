class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # obtain count of each of the numbers present in the list

        count = {}

        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
        print(count)
        # for each number, place in a bucket frequency
        
        frequency = [0] * len(nums)

        for num in count.keys():
            print(num, frequency)
            frequency[count[num]-1] = num
        

        # iterate through the buckets from the least to most until len(result) becomes == k
        print(frequency)
        result = []
        progress = len(frequency) -1
        while not len(result) == k:
            print(frequency[progress])
            if frequency[progress] != 0:
                result.append(frequency[progress])
            progress -= 1

        return result   
