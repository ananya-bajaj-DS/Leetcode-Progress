class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # l=0
        # r=1
        # maxP=0

        # while r<len(prices):
        #     # print(prices[l] ,prices[r])
        #     if prices[l] > prices[r]:
        #         l=r
        #         # r+=1
        #     else:
        #         profit = prices[r] - prices[l]
        #         if maxP<profit:
        #             maxP=profit
        #         # maxP = max(maxP, profit)
        #     r+=1
        # return maxP

        l=0
        h=0
        max_diff=0

        if len(prices) <=1:
            return 0

        for h in range(1,len(prices)):
            if l>=len(prices):
                return max_diff
            if prices[h] > prices[l]:
                diff = prices[h] - prices[l]
                max_diff = max(max_diff, diff)
             
            else:
                l = h
        return max_diff

        


 
        






            


        
          
        