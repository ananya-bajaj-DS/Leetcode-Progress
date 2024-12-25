class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False
        
        hm_s = defaultdict(int)
        hm_t = defaultdict(int)

        for i in range(len(s)):
            hm_s[s[i]] +=1
        for i in range(len(t)):
            hm_t[t[i]] +=1
        if hm_s!=hm_t:
            return False
        return True


        
        
        