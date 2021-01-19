class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        countR = 0
        countL = 0
        for i in range(len(s)):
            if s[i] == "R":
                countR += 1
            else:
                countL += 1
            if countR == countL and countR != 0 and countL !=0:
                sum += 1
                countR = 0
                countL = 0
        return sum