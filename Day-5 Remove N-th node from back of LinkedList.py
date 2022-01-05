class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=head
        while n:
            x=x.next
            n-=1
        if x==None: return head.next
        new=head
        while x.next:
            x=x.next
            new=new.next
        new.next=new.next.next
        return head

# Problem link
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/