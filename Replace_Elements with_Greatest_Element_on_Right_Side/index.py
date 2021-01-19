class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        t = arr[-1]
        arr[-1]=-1
        n = len(arr)
        for i in range(n-2,-1,-1):
            temp = arr[i]
            arr[i] = t
            t = max(t, temp)
        return arr
            