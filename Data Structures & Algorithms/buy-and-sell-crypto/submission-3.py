class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy= 0
        sell = buy+1

        while(sell < len(prices)):
            res = max(res,prices[sell]-prices[buy])
            if(prices[sell] < prices[buy]):
                buy = sell
                sell = buy+1
            else:
                sell += 1
        
        return res
        