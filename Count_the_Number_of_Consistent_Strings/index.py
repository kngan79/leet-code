class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for w in words:
            check = True
            for i in range(len(w)):
                if w[i] not in allowed: check = False
            if check == True:
                count += 1
        return count
