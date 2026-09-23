class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[[]]
        for num in nums:
            nr=[]
            for p in result:
                for i in range(len(p)+1):
                    np=p[:i]+[num]+p[i:]
                    nr.append(np)
            result=nr
        return result