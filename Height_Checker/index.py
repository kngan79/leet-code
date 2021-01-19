class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        srt = sorted(heights)
        count = 0
        for i in range(len(srt)):
            if srt[i] != heights[i]:
                count += 1
        return count