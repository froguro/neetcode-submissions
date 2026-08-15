# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        brute force: linearly go to the end of the list while storing all the entries in a list. O(N) time but O(N) space
        two pass solution: go through once to find the length, then remove the (length - n)th item
        """

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        remove = length - n
        if remove == 0:
            head = head.next
            return head
        i = 0

        curr = head
        for i in range(remove - 1):
            curr = curr.next
        print(curr.val)
        curr.next = curr.next.next

        return head