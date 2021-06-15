class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={} #creating a dictionary
        for values in nums: #adding values to dic
            if values not in dic:
                dic[values]=1
            elif values in dic:
                dic[values]+=1
        for i in range(len(dic)):#checking the dictionary
            if dic[nums[i]]>1:
                return True
        return False
            
        
            
                
