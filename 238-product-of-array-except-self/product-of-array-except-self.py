class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[1] *len(nums)
        prefix[0] = nums[0]
        sufix=[1] *len(nums)
        sufix[len(nums)-1] = nums[len(nums)-1]

        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
    

        j = len(nums)-2 
        for i in (nums[len(nums)-2::-1]):
            sufix[j] = i * sufix[j+1]
            j-=1
 

        res = [1] * len(nums) 
        res[0] = sufix[1]
        res[len(nums)-1] = prefix[len(nums)-2]
        
        for n in range(1,len(nums)-1): 
            res[n] = prefix[n-1] * sufix[n+1]
            
        return res
        