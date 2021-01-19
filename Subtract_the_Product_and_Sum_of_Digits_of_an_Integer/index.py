class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])
        product = 1
        for i in range(len(s)):
            product *= int(s[i])
        return product - sum