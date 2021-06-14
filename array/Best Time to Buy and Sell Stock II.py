class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0 
        
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: #checking the previous prices with the next one
                total+= prices[i]-prices[i-1] #updating the total profit
        return total        
                
