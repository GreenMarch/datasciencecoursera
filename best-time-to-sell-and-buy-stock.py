class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')

        profit = 0          
        for price in prices:
            if price < buy_price:
                buy_price = price
            if price - buy_price > profit:
                profit = price - buy_price
        return profit   
