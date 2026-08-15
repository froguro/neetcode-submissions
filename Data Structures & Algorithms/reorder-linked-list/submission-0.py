# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        upperHalf = slow.next

        # reverse the second half
        prev = slow.next = None
        while upperHalf:
            temp = upperHalf.next
            upperHalf.next = prev
            prev = upperHalf
            upperHalf = temp
        
        curr = head
        while prev:
            temp1, temp2 = curr.next, prev.next
            curr.next = prev
            prev.next = temp1
            curr = temp1
            prev = temp2
