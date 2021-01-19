class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            num = 0
            while nums[i] > 0:
                num += 1
                nums[i] //= 10
            if num % 2 == 0:
                res += 1
        return res
        