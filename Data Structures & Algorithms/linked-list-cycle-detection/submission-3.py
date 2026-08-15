# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if there is a cycle, then the tail node will 
        # point to the "index" of the beginning of the cycle
        # fast and slow ptr
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False 