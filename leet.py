class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0 # Left pointer to track the position of the next non-zero element
        for r in range(len(nums)):
            if nums[r] != 0:
            # Swap non-zero element with the element at the left pointer
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print(nums)  
