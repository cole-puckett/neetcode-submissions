class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        answer = [1] * len(nums)

        zero1 = False
        zero2 = False

        for num in nums:
            if num == 0:
                if zero1:
                    zero2 = True
                else:
                    zero1 = True
            else:
                total = total * num
        
        if zero2:
            submit = [0] * len(nums)
            return submit

        if zero1:
            submit = [0] * len(nums)
            for i in range(len(answer)):
                if nums[i] == 0:
                    submit[i] = total
                    return submit

        for i in range(len(answer)):
            answer[i] = int(total / nums[i])

        return answer