class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        for i in range(0,len(nums)+1):
            if i in nums:
                continue
            else:
                p=i
        return p