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
        if not heights:
            return 0

        max = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                potential_max = self.lower(heights[i], heights[j]) * self.length(i, j)
                if potential_max > max:
                    max = potential_max
        return max

    def lower(self, i, j) -> int:
        if i > j:
            return j
        else:
            return i
    def length(self, i, j) -> int:
        if i > j:
            return (i - j)
        else:
            return (j - i)