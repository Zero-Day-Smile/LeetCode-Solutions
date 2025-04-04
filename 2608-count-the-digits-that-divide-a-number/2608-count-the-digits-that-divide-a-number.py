class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        a=[]
        c=0
        while n>0:
            s=n%10
            a.append(s)
            n=n//10
        for i in a:
            if num%i==0:
                c+=1
        return c