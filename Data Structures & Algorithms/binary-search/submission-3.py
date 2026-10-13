class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            midpoint= (r-l)//2

            if nums[midpoint]<target:
                l = midpoint+1
            elif nums[midpoint]>target:
                r = midpoint
            else:
                return midpoint
        return -1