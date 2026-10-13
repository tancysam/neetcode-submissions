class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.arr = []
        for num in nums:
            if len(self.arr) < k:
                heapq.heappush(self.arr,num)
            else:
                heapq.heappush(self.arr,num)
                heapq.heappop(self.arr)

    def add(self, val: int) -> int:

        heapq.heappush(self.arr,val)
        heapq.heappop(self.arr)
        
        return self.arr[0]
