class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        for number in nums:
            if number in temp:
                return True
            else:
                temp.append(number)
        return False