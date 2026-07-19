class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        while l<=r:
            m = (l + r) // 2


            if matrix[m][0] <= target and matrix[m][len(matrix[m])-1] >= target:

                submatrix = matrix[m]

                l = 0
                r = len(submatrix) - 1


                while l <=r:
                    m = (l+r) // 2

                    if submatrix[m] == target:
                        return True
                    elif submatrix[m] < target:

                        l = m+1
                    elif submatrix[m] > target:

                        r = m - 1

            elif matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        
        return False