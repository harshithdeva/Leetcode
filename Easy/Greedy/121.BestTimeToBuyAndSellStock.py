from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i,price in enumerate(prices):
            if price < min_price:
                min_price = price
            if i == 0:
                continue
            potential_profit = price-min_price
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
    


            
