class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX_PROF=0
        min_buy=prices[0]
        for sell in prices:
            MAX_PROF=max(MAX_PROF,sell-min_buy)
            min_buy=min(min_buy,sell)
        return MAX_PROF    
        