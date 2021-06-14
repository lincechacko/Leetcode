class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        traingle=[[1]*i for i in range(1 ,rowIndex+2)]
        i=1
        while i <rowIndex+1:
            for j in range(1,len(traingle[i-1])):
                traingle[i][j]=traingle[i-1][j]+traingle[i-1][j-1]
            i+=1
        return traingle[rowIndex]    
                  
