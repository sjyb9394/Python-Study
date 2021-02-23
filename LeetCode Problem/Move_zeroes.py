# Linke: https://leetcode.com/problems/move-zeroes/submissions/
# Problem:
#   Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
  
  
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """

      count = 0
      i = 0

      while i < len(nums):
          if nums[i] == 0:
              count +=1
              del nums[i]
              i-=1
          i+=1

      for _ in range(count):
          nums.append(0)
