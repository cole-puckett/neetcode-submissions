class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if j != i:
                    answer[j] = answer[j] * nums[i]
        
        return answer