class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(not prices):
            return 0
        profit = 0
        buy = prices[0]
        for v in prices:
            buy = min(buy, v)
            profit = max(profit, v-buy)
        return profit
            