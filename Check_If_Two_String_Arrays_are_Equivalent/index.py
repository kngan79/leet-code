class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_concat = ""
        word2_concat = ""
        for i in range(len(word1)):
            word1_concat += word1[i]
        for j in range(len(word2)):
            word2_concat += word2[j]
        if word1_concat == word2_concat:
            return True
        else:
            return False