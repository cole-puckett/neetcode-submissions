import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for number in nums:
            counter[number] += 1
        
        arr = collections.deque()

        for key in counter.keys():
            arr.append([counter[key], key])

        arr = collections.deque(sorted(arr))

        result = []

        while len(result) < k:
            result.append(arr.pop()[1])
        return result