import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min-heap implementation

        countermap = {}
        for num in nums:
            countermap[num] = 1 + countermap.get(num, 0)
        
        heap = []

        for number, count in countermap.items():
            heapq.heappush(heap, [-count, number])
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res