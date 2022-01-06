# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow=head
        fast=head.next #fast=slow*2
        while(fast and fast!=slow and fast.next):
            slow=slow.next
            fast=fast.next.next #fast=slow*2
            
        if fast==slow: #hasCycle 
            while(slow.next!=head):
                slow=slow.next
                head=head.next
            return head
        else:
            return None
        

# Problem link
# https://leetcode.com/problems/linked-list-cycle-ii/

# source
# https://leetcode.com/mayura_8499