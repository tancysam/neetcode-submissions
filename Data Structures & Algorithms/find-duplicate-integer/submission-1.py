class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]

        step = 0

        while step < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                return nums[slow]
            
            step += 1
        