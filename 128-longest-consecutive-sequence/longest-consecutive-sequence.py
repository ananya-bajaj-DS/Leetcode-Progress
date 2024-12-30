class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset = set(nums)
        length = 0
        longest = 0

        for n in hashset:
            if (n-1) not in hashset:
                length = 1
          
                while (n+length) in hashset:
                        length+=1 
                if longest < length:
                    longest = length
                # longest = max(longest,length)
        return longest


        