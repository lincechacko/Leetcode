class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        
        def pal(l,r):
            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break
                l-=1
                r+=1
            return l+1,r   
        
        start=0
        end=0
       
        for i in range(n):
            l,r=pal(i,i)
            if (r-l) > (end-start):
                end=r
                start=l
            l,r=pal(i,i+1)
            if (r-l) > (end-start):
                end=r
                start=l
        return s[start:end]           
                
                
            
            
