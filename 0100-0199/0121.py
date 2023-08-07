"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for sell_price in prices[1:]:
            if sell_price > buy_price:
                max_profit = max(max_profit, sell_price - buy_price)
            else:
                buy_price = sell_price
        return max_profit
