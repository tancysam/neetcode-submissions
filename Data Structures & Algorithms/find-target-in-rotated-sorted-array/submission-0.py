class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Need to reduce list to the portion where target is in
        # then need to binary search the list for target
        l = 0
        r = len(nums) -1
        print("1")
        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
    
        print("2")
        numsMin = l
        l = 0
        r = len(nums) -1

        if nums[numsMin] <= target and nums[l] > target:
            l = numsMin
            r = len(nums) -1
        elif nums[numsMin] > target and nums[r] < target:
            l = 0
            r = numsMin -1
        else:
            return -1
        print("3")
        
        while l<r:
            m = (l+r) //2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m - 1

        return -1
