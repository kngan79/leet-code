class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        copy_nums = nums[:]
        largest_num = max(copy_nums)
        i = nums.index(largest_num)
        copy_nums.remove(largest_num)
        second_largest_num = max(copy_nums)
        j = nums.index(second_largest_num)
        result.append(nums[i])
        result.append(nums[j])
        return (result[0]-1)*(result[1]-1)