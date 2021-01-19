class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        s= ""
        if n%2 == 0:
            countx = n-1
            for i in range(0,countx):
                s += "x"
            s += "y"
            return s
        if n%2 ==1:
            countx = n
            for i in range(0,countx):
                s += "x"
            return s
            