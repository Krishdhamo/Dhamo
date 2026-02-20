# # Input: numRows = 5
# # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# class Solution:
#     def generate(self, numRows):
#         triangle = []
#         for i in range(numRows):# Loop through each row index from 0 to numRows-1
#             row = [1] * (i + 1)
#             for j in range(1, i):
#                 row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]# Calculate the value of the current element by summing the two elements directly above it in the previous row
#             triangle.append(row)
#         return triangle
    
# s = Solution()
# print(s.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]class Solution(object):


def longestCommonPrefix(self, strs):
        if not strs:
            return ""

    # Find the minimum length string in the list
        min_str = min(strs, key=len)

    # Check each character of the minimum string
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]

        return min_str
# s = Solution()
