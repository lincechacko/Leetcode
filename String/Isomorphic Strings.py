class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def isomorphic(words):
            output=[]
            dic={}
            num=1
            for i in words:
                if i not in dic:
                    dic[i]=num
                    num+=1
                output.append(dic[i])
            return output
        return isomorphic(s)==isomorphic(t)
        
        
            
