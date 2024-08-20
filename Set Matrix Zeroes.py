class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    for p in range(0,len(matrix[i])):
                        if matrix[i][p]!=0:
                            matrix[i][p]='V'
                    for k in range(0,len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j] = 'V'
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'V':
                    matrix[i][j]=0