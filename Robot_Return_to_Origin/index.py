class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        :moveUD:int
        :moveLR:int
        """
        moveUD = 0
        moveLR = 0
        for i in range(len(moves)):
            if moves[i] == "U":
                moveUD += 1
            if moves[i] == "D":
                moveUD -= 1
            if moves[i] == "L":
                moveLR -= 1
            if moves[i] == "R":
                moveLR += 1
        if moveUD ==0 and moveLR ==0:
            return True
        else:
            return False