class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        l = 0
        r = len(nums) -1

        # Find inflexion point
        while l < r:

            m = (l + r)//2

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m 
            

        #now that l is the inflexion point,

        inflexionPoint = l
        l, r = 0, len(nums)-1
        if nums[0] <target < nums[inflexionPoint]:
            r = inflexionPoint
        else:
            l = inflexionPoint

        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m 

        return -1