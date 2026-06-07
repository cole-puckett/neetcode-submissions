class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max_profit = 0

        ''' we want to move our window based on if we see a 
            smaller minimum or a larger maximum
        '''

        for i in range(len(prices)):
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
            
        return max_profit