class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        max_profit = 0

        ''' we want to move our window based on if we see a 
            smaller minimum or a larger maximum
        '''

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if max_profit < profit:
                    max_profit = profit
            else:
                left = right
            
            right += 1
        
        return max_profit