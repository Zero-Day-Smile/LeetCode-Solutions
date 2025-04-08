class Solution:
    def reverse(self, x: int) -> int:
        mini=-2**31
        maxi=2**31-1
        if x>=0:
            s=int(str(x)[::-1])
        else:
            s=-int(str(-x)[::-1])
        if s>maxi or s<mini:
            return 0
        return s