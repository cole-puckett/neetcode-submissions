from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort implementation

        countermap = defaultdict(int)

        for num in nums:
            countermap[num] += 1

        frequencyList = [[] for i in range(len(nums) + 1)]

        for number, count in countermap.items():
            frequencyList[count].append(number)
        
        result = []

        for i in range(len(frequencyList) - 1, 0, -1):
            for number in frequencyList[i]:
                result.append(number)

                if len(result) == k:
                    return result
        