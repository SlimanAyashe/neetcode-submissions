class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMaxProfit = 0
        maxFromLeft = prices[-1]
        for price in reversed(prices):
            if price < maxFromLeft and currMaxProfit < maxFromLeft - price : 
                currMaxProfit = maxFromLeft - price
            elif price >= maxFromLeft:
                maxFromLeft =  price
        return currMaxProfit