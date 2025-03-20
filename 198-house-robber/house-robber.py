class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob2(nums, i, memo):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            
            memo[i] = max(nums[i] + rob2(nums, i+2, memo), rob2(nums, i+1, memo))
            return memo[i]

        
        memo = [-1]*len(nums)
        return rob2(nums,0,memo)


    

        