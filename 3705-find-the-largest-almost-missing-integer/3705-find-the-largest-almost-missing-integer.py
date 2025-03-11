from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        frequency=Counter()
        for i in range(n-k+1):
            subarray=nums[i:i+k]
            frequency.update(subarray)
        count={num:0 for num in nums}
        for i in range(n-k+1):
            subarray=nums[i:i+k]
            for num in set(subarray):
                count[num]+=1
        largest=-1
        for num in nums:
            if count[num]==1:
                largest=max(largest,num)
        return largest
