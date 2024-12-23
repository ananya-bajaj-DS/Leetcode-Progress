class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = defaultdict(list)
        for word in strs:
            freq = [0] * 26 
            for char in word:
                freq[ord('a') - ord(char)] +=1
            hm[tuple(freq)].append(word) 
        
        return (hm.values()) 
        