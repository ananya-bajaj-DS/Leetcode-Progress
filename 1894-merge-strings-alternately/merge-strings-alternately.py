class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1)>len(word2):
            longer_word = word1
        else:
            longer_word = word2
        word3=''
        for i in range(len(longer_word)):
                ch1 = word1[i] if i<len(word1) else ''
                ch2 = word2[i] if i<len(word2) else ''
                word3+=ch1+ch2
                print(word3)
        return word3
        