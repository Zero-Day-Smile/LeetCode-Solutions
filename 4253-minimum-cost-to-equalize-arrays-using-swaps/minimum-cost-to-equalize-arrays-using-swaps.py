class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        diff=defaultdict(int)
        for x in nums1:
            diff[x]+=1
        for x in nums2:
            diff[x]-=1
        ans = 0
        for x in diff:
            if diff[x]%2!=0:
                return -1
            ans+=abs(diff[x])//2
        return ans//2