class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]]=i
        
        for i in range(len(nums)):
            if (target - nums[i]) in hm:
                idx = hm.get(target - nums[i])
                if idx!=i:
                    return  [i,idx]
        