class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            x=str(x)
            if x==x[::-1]:
                return True
            else:
                return False
        else :
            return False