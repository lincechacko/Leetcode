class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        value={}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in value:
                return[value[diff],i+1]
            else:
                value[numbers[i]]=i+1
