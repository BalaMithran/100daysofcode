class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxsofar= 0
        minprice = prices[0]
        for i in prices:
            minprice = min(minprice , i)
            maxsofar = max(maxsofar,(i-minprice))
        return maxsofar
            
        

# problem link
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/