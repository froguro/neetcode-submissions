class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        buy low, sell high for maximum profit

        brute force: n^2, for each i search for j that maximizes the profit for i

        sliding window:
        consider i as the selling value, keeping track of the lowest values?
        """

        minBuy = float('inf')
        buyIdx = 0
        res = 0
        for i in range(len(prices)):

            res = max(res, prices[i] - minBuy)

            if prices[i] < minBuy: 
                minBuy = prices[i]
                buyIndex = i

        return res