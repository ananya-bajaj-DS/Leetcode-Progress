class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        l = 0 
        max_len=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(count.values())

            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1

            max_len = max((r-l+1), max_len )

        return max_len

        