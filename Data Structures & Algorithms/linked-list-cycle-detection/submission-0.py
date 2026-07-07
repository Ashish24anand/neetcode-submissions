# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_next = {}
        while head:
            if head.val in val_next:
                if head.next == val_next[head.val]:
                    return True
            else:
                val_next[head.val] = head.next
            head = head.next
        return False
            

        