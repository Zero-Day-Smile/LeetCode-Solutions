class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            digits=str(n)
            total=0
            for digit in digits:
                total+=int(digit)**2
            n=total
        return n==1
