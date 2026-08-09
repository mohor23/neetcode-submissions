class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for price in range(1,len(prices)):
            min_price=min(min_price,prices[price])
            max_profit=max(max_profit,prices[price]-min_price)
        return max_profit
