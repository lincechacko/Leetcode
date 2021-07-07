class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=list(reversed(s))
        for i in s:
            if i==" ":
                if count>=1:
                    return count
                
            else:
                count+=1
                
        return count        
