# Link  : https://leetcode.com/problems/single-number/
# Problem:
#   Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#   Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        
        for i in range(len(nums)):
            answer ^= nums[i]
        
        return answer
