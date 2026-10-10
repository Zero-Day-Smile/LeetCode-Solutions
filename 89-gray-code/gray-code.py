class Solution:
    def grayCode(self, n: int) -> list[int]:
        ans=[0]
        for i in range(n):
            s=len(ans)
            for j in range(s-1,-1,-1):
                ans.append(ans[j]+2**i)
        return ans