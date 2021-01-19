class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        i = 0
        j = 0
        check = {}
        while i < len(arr):
            while j < len(arr) and arr[j] == arr[i]:
                j +=1
            count = j - i
            if check.get(count, False) ==  True:
                return False
            check[count] = True
            i = j
        return  True