class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j] ,matrix[j][i] = matrix[j][i] , matrix[i][j]
            matrix[i] = matrix[i][::-1]
        
                
# Problem link        
# https://leetcode.com/problems/rotate-image/