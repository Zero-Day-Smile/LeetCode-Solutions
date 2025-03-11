class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs=str(x)
        n=len(xs)
        for i in range(n):
            if xs[i]!=xs[-i-1]:
                return False
        return True
            