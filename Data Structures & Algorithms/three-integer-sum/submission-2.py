class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hashtable = set()
        final = []
        nums_sort = nums.sort()

        for i in range(0, len(nums)):
            subresult = 0 - nums[i]
            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2:
                temp_subresult = nums[p1] + nums[p2]
                if temp_subresult == subresult and (nums[i],nums[p1],nums[p2]) not in hashtable:
                    hashtable.add((nums[i],nums[p1],nums[p2]))
                    final.append([nums[i],nums[p1],nums[p2]])
                else:
                    if temp_subresult <= subresult:
                        p1 += 1
                    elif temp_subresult > subresult:
                        p2 -= 1

        return final
                        
                
                    
