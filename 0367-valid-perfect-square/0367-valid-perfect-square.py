class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0 :
            return False

        num1 = int(num**0.5)

        if num1*num1 == num :
            return True
        else :
            return False