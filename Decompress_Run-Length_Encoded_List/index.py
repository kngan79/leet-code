class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i+1]
            for j in range(freq):
                r.append(val)
        return r
            
        