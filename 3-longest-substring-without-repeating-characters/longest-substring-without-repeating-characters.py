class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        ls = []
        j = 0
        i = 0
        cnt = 0
        max_ct = 0

        while i<len(s) and j<len(s):
            if s[j] not in ls:
                ls.append(s[j])
                j+=1
                cnt+=1
                max_ct = max(max_ct, cnt)
            else:
                i+=1
                ls.pop(0)
                cnt-=1
                
        return max_ct

            

        