class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxS = 1; 
        low = 0; 
        maxP = 0; 

        while(maxS < len(prices)):
            if(prices[low]< prices[maxS]):
                price = prices[maxS] - prices[low]
                maxP = max(maxP, price);
            else:
                low = maxS
            maxS += 1

        

        return(maxP)


        