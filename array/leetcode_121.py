# Problem: Best Time to Buy and Sell Stock
# LC: #121
# Approach: Track min price + max profit in single pass
# TC: O(n) | SC: O(1)
# Pattern: Greedy — update min seen so far, calculate profit at each step


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')  # infinitely large number
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price        # update lowest price seen
            
            profit = price - min_price            # profit if sold today
            
            if profit > max_profit:
                max_profit = profit       # update best profit seen

        return max_profit