class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        b=""
        counta = 0
        countb= 0
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[0:len(s)//2] 
        b = s[len(s)//2:]
        for i in range(len(a)):
            if a[i] in vowels:
                counta += 1
        for j in range(len(b)):
            if b[j] in vowels:
                countb += 1
        if counta == countb:
            return True
        else:
            return False