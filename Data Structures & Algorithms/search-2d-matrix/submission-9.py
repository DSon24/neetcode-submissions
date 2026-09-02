class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1 find the row
        l,r = 0,len(matrix)-1
        while l <= r:
            mid = (l + r)//2 
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        else:
            return False
        
        #2 find the target
        l,r = 0,len(matrix[row])-1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return False        