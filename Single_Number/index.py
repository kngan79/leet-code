from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        f = defaultdict(lambda: 0, {})
        for i in range(len(nums)):
            f[nums[i]] += 1
        for i in range(len(nums)):
            if f[nums[i]] == 1:
                return nums[i]
        