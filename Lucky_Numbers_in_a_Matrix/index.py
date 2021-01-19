class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ma = []
        mi = []
        for row in matrix:
            mi.append(min(row))
        n = len(matrix)
        m = len(matrix[0])
        for i in range(m):
            x = -100000000000
            for j in range(n):
                x = max(x, matrix[j][i])
            ma.append(x)
        result = []
        for i in range(len(mi)):
            for j in range(len(ma)):
                if mi[i] == ma[j]:
                    result.append(mi[i])
        return result