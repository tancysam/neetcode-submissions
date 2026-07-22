class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = []

        for num in nums:
            if len(arr) < k:
                heapq.heappush(arr,num)
            elif arr[0] < num:
                heapq.heappop(arr)
                heapq.heappush(arr,num)
        
        return arr[0]