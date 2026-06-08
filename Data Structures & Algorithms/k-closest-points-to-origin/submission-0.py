import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2) ** .5
            heapq.heappush(heap, (distance, point))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result