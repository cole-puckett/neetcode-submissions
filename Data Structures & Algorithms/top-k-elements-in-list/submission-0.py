class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        common = count.most_common(k)
        answer = []
        for pair in common:
            answer.append(pair[0])
        return answer