class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prof=float('inf')
        max_prof=0
        for price in prices:
            min_prof=min(min_prof,price)
            max_prof=max(max_prof,price-min_prof)
        return max_prof


        