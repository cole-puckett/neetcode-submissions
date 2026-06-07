class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' have to multiply the shorter bar height by the difference between the two
        bars (pointers/indices). a few cases:
        the max is in the middle
        the max is on the right or left - 

        we have to walk the pointers in to find the maximum possible capacity

        the max is the very outside edges - easiest to compute and first check

        brute force solution - nested loops to compare every index with every other index
        '''
        left = 0
        right = len(heights) - 1
        maximum = 0

        if not heights:
            return 0
        elif right == 0:
            return 0

        while left < right:
            potential_max = self.lower(heights[left], heights[right]) * (right - left)
            if potential_max > maximum:
                maximum = potential_max
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maximum

    def lower(self, left, right) -> int:
        if left > right:
            return right
        else:
            return left