class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0   
        for i in range(len(S)):
            for j in range(len(J)):
                if S[i] == J[j]:
                    count = count + 1
        return count
                    
            