class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value={}
        for num in nums:
            if num not in value:
                value[num]=1
            if value[num] > len(nums)//2:
                return num
            else:
                value[num]+=1
                
