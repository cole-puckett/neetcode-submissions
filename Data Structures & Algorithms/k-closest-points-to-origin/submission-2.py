import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2) ** .5
            heap.append([distance, point[0], point[1]])
        
        heapq.heapify(heap)
        result = []
        for i in range(k):
            point = heapq.heappop(heap)
            result.append([point[1], point[2]])

        return result