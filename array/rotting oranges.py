class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        n=len(grid)
        m=len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
        
        minute=0
        prev=fresh
        
        while True:
            cp=copy.deepcopy(grid)
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==2:
                        for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                            if 0<=r<n and 0<=c<m and cp[r][c]==1:
                                cp[r][c]=2
                                fresh-=1
                       
            if prev==fresh:
                break
            minute+=1
            grid=cp
            prev=fresh
            
        if fresh>0:
            return -1
        else:
            return minute
            
