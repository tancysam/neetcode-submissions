class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr=[]

        for point in points:
            dist = -self.distance(point)

            if len(arr) < k:
                heapq.heappush(arr,[dist,point])
            elif dist > arr[0][0]:
                heapq.heappop(arr)
                heapq.heappush(arr,[dist,point])
        
        return [i[1] for i in arr]
    
    def distance(self, points):
        return (points[0]**2 + points[1]**2)**0.5