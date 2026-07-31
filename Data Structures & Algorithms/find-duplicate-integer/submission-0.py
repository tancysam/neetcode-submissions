class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        obj = set()

        for num in nums:
            if num in obj:
                return num
            else:
                obj.add(num)
        
        