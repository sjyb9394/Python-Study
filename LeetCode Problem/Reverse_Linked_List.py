# Link: https://leetcode.com/problems/reverse-linked-list/
# Problem:
#   Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        answer = None
        
        while head is not None:
            nextNode = head.next
            head.next = answer
            answer = head
            head = nextNode
        
        return answer
