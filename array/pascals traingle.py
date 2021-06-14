class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        traingle = [[1]*i for i in range(1,numRows+1)]
        i=1
        while i < numRows:
            for j in range(1 , len(traingle[i-1])):
                traingle[i][j]=traingle[i-1][j]+traingle[i-1][j-1]
            i+=1
        return traingle
            
                    
