class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestbuyseen = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            if(prices[i]-lowestbuyseen>maxprofit):
                maxprofit = prices[i]-lowestbuyseen
            if(prices[i]<lowestbuyseen):
                lowestbuyseen = prices[i]
        
        return maxprofit