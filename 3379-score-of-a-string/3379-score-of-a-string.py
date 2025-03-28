class Solution:
    def scoreOfString(self, s: str) -> int:
        num=[]
        a=0    
        for ch in s:
            num.append(ord(ch))
        for i in range(len(num)-1):
            a=a+abs(num[i]-num[i+1])
        return a
        