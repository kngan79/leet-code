def numToChar(num):
    return chr(num - 1 + ord('a'))

class Solution(object):
    
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapp = {}
        j = 'a'
        for i in range(26):
            mapp[i+1] = j
            j = chr(ord(j) + 1)
        
        i = 0
        result = ""
        while i < len(s):
            num = 0
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                i += 3
            else:
                num = int(s[i])
                i += 1
            result += mapp[num]
            
        return result