class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        a = len(str1)
        b = len(str2)
        print(a,b)

        def gcd(a,b):
            # base case
            if b == 0:
                return a
            else:
                return gcd(b, a%b)
                

        if str1+str2!=str2+str1:
            return ""
        
        if a>b: 
            final_len = gcd(a,b)
            return str1[:final_len]
        else:
            final_len = gcd(b,a)
            return str2[:final_len]
        