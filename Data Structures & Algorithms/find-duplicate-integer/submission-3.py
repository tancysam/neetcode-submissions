class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]

        step = 0

        while step <= len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
            step += 1
        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        