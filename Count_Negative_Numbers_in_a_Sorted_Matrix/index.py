class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(grid)):
            if grid[i] < 0:
                sum += 1
            for j in range(len(grid[i])):
                if grid[i][j] <0:
                    sum += 1
        return sum