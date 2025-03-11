class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c={}
        for char in s:
            if char in c:
                c[char]+=1
            else:
                c[char]=1
        counts=list(c.values())
        return len(set(counts))==1

