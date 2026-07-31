class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Need to reduce list to the portion where target is in
        # then need to binary search the list for target
        l = 0
        r = len(nums) -1

        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
    

        numsMin = l
        l = 0
        r = len(nums) -1

        if nums[numsMin] <= target <= nums[r]:
            l = numsMin
            r = len(nums) -1
        else: 
            l = 0
            r = numsMin -1

        
        while l<r:

            m = (l+r) //2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if nums[l] == target:
            return l
        else:
            return -1
