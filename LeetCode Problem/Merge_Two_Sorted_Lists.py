# Link: https://leetcode.com/problems/merge-two-sorted-lists/
    
# Problem:
#   Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        cur = answer
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
    
            cur = cur.next
            
        if l1 is None and l2 is not None:
            cur.next = l2
        elif l1 is not None and l2 is None:
            cur.next = l1
        
        return answer.next
