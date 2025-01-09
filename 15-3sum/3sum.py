class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
 
        
        nums.sort()
       
        i = 0
        ls = []
        res=[]
       
        
        while i < len(nums):
            
            j=i+1
            k = len(nums)-1
            while j<k:
                if nums[j] + nums[k] == -nums[i]:
                    res = []
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(nums[k])
                    if res not in ls:
                        ls.append(res)
                  
                    j +=1
                    k -=1
                    
                elif nums[j] + nums[k] < -nums[i]:
                    j+=1
                else:
                    k-=1 
 
            i+=1
           
           
            
        return ls






        