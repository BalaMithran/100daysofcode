# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        if head== None:
            return head
        next = head.next
        while next!= None:
            head.next = new
            new = head
            head = next
            next = head.next
        head.next = new
        return head
            
            
        
# Problem link
# https://leetcode.com/problems/reverse-linked-list/