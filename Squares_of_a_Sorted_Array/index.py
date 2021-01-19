class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in A:
            i *= i
            result.append(i)
        result.sort()
        return result