class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.arr = [k,[]]
        for num in nums:
            if len(self.arr[1]) < k:
                heapq.heappush(self.arr[1],num)
            else:
                heapq.heappush(self.arr[1],num)
                heapq.heappop(self.arr[1])

    def add(self, val: int) -> int:
        if len(self.arr[1]) < self.arr[0]:
            heapq.heappush(self.arr[1],val)
        else:
            heapq.heappush(self.arr[1],val)
            heapq.heappop(self.arr[1])

        return self.arr[1][0]
