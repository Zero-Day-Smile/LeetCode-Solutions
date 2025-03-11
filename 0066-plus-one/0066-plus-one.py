class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int("".join(map(str,digits)))
        n+=1
        n=list(map(int,str(n)))
        return n