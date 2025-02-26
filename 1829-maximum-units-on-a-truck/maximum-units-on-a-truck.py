class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes_s = sorted(boxTypes, key=lambda x : x[1], reverse=True)

        sz=0
        units=0
       
        for i in boxTypes_s:
            if sz + i[0]>truckSize:
                return  units + i[1]*(truckSize-sz)
            sz += i[0]
            units += i[0]*i[1]
        
        return units

            

            


        

            

        