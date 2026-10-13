class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        triplets_check = set()

        for i in range(len(nums)):
            p1 = i
            p2 = len(nums)-1

            while p1 < p2:
                if nums[p1] + nums[p2] + nums[i] == 0 and str([nums[p1],nums[p2],nums[i]]) not in triplets_check:
                    triplets.append([nums[p1],nums[p2],nums[i]])
                    triplets_check.add(str([nums[p1],nums[p2],nums[i]]))
                    p1 += 1
                    p2 -= 1                
                else:
                    p1 += 1
                    p2 -= 1

        return triplets
                