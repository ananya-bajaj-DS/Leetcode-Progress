class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l=0
        r=1
        maxP=0

        while r<len(prices):
            # print(prices[l] ,prices[r])
            if prices[l] > prices[r]:
                l=r
                # r+=1
            else:
                profit = prices[r] - prices[l]
                if maxP<profit:
                    maxP=profit
                # maxP = max(maxP, profit)
            r+=1
        return maxP
        


 
        






            


        
          
        