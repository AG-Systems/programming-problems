class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movement = [0,0]
        for x in moves:
            if x == "U":
                movement[1] += 1
            elif x == "D":
                movement[1] -= 1
            elif x == "L":
                movement[0] += 1
            elif x == "R":
                movement[0] -= 1
        if movement[0] == 0 and movement[1] == 0:
            return True
        else:
            return False
