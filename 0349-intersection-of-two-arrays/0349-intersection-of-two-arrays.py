class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for x in nums1:
            if x in nums2 and x not in r:
                r.append(x)
        return r