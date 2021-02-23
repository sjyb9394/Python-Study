# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Reference: https://www.youtube.com/watch?v=jSfDPVIYe1s&ab_channel=jayatitiwari
# Problem: 
#   Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#   Find all the elements of [1, n] inclusive that do not appear in this array.
#   Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            curr = abs(nums[i])
            nums[curr-1] = -(abs(nums[curr-1]))
            
        for i in range(len(nums)):
            if nums[i] > 0:
                answer.append(i+1)
            
        return answer
