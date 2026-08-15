# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        # verificar fast.next para iterar next.next sem problemas
        while fast and fast.next:
            slow = slow.next
            fast = (fast.next).next
            # confere objeto node ao inves de val em caso de duplicacoes
            if slow == fast:
                return True
        return False