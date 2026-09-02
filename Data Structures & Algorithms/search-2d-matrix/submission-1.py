class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # Step 1: Find the correct row
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            return False

        # Step 2: Binary search inside that row
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
