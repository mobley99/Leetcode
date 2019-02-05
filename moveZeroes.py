class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = 0
        count = i
        
        while i < len(nums):
            if count >= len(nums):
                break
            if nums[i] == 0:
                for j in range(i,n-1):
                    nums[j] = nums[j+1]
                nums[n-1] = 0
            else:
                i+= 1
            count += 1
        
