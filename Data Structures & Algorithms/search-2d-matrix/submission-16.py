class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        row = -1
        while(l <= r):
            m = l + (r-l)//2
            if(target >= matrix[m][0] and target <= matrix[m][-1]):
                if(target == matrix[m][0] or target ==matrix[m][-1]):
                    return True
                ll = 0
                rr = len(matrix[m])
                while(ll <= rr):
                    mm = ll + (rr-ll)//2
                    if(matrix[m][mm] == target):
                        return True
                    elif(matrix[m][mm] > target):
                        rr = mm-1
                    else:
                        ll = mm+1
                return False
            elif(target<matrix[m][0]):
                r = m-1
            else:
                l = m+1
        
        return False
            