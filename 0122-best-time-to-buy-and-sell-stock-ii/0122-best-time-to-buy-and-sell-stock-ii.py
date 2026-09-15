class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0 
        n = len(prices)
        
        for i in range(n-1):
            if prices [i+1]>prices[i]:
                profit += (prices[i+1]-prices[i] )

        return profit 