class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=[]
        for n in s:
            num.append(ord(n)-96)
        num=''.join(map(str,num))
        for i in range(k):
            sumd=0
            for digit in num:
                sumd+=int(digit)
            num=str(sumd)
        return int(num)