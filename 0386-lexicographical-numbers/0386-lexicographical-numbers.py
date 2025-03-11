class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sort=sorted(map(str,range(1,n+1)))
        return list(map(int,sort))
