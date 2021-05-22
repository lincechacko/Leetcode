class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        fsum=0
        tsum=nums[0]
        i=0
        for i in range(len(nums)):
            fsum=max(nums[i],fsum+nums[i])
            tsum=max(fsum,tsum)
        return tsum
        
