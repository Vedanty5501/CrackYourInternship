class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=prices[0]
        max_prof = 0
        for i in range(1,len(prices)):
            if prev>prices[i]:
                prev=prices[i]
            if prices[i]-prev>max_prof:
                max_prof=prices[i]-prev
        return max_prof