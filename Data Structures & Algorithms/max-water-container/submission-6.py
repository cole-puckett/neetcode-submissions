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

        # if the input array is empty or of size 1
        if not heights or right == 0:
            return 0

        while left < right:
            # calculate current max height and see if it's larger than our maximum
            potential_max = self.lower(heights[left], heights[right]) * (right - left)
            if potential_max > maximum:
                maximum = potential_max

            # if the left wall is shorter than the right wall, move it forward
            if heights[left] < heights[right]:
                # set the current height as our max height
                left_max = heights[left]
                left += 1
                # skip past all walls that are shorter
                while heights[left] < left_max and left < right:
                    left += 1
            
            # else move the right boundary
            elif heights[right] < heights[left]:
                # set the current height as our max height
                right_max = heights[right]
                right -= 1
                # skip past all walls that are shorter
                while heights[right] < right_max and right > left:
                    right -= 1
            
            # then two wall are of the same height
            else:
                # we want to move the wall with the next largest height
                if heights[left + 1] > heights[right - 1]:
                    left += 1
                else:
                    right -= 1
        
        return maximum

    def lower(self, left, right) -> int:
        if left > right:
            return right
        else:
            return left