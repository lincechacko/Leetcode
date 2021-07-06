class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={")":"(","]":"[","}":"{"}
        for p in s:
            if p in dic.values():
                stack.append(p)
            elif stack and dic[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]    
            
            
