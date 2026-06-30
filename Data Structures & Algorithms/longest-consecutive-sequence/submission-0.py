class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        global_max = 0

        for num in nums:
            if num-1 not in numSet:
                curr = num
                length = 1
                while curr + 1 in numSet:
                    length += 1
                    curr += 1
                if length > global_max:
                    global_max = length
        
        return global_max
            

