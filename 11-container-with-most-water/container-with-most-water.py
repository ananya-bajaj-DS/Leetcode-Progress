class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height)-1
        maxArea = float('-inf')

        def calculateArea(l,r):
            b = abs(l-r)
            if height[l]<height[r]:
                h = height[l]
            else:
                h = height[r]

            A = b*h
            return A


        while l<r:
            Area = calculateArea(l,r)
            if maxArea > Area:
                 maxArea = maxArea
            else:
                maxArea = Area

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxArea



        
        