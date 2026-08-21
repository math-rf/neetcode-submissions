# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # aponta para o comeco da lista
        left = dummy
        right = head

        # loop para encontrar valor a ser excluido
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # loop para left chegar ate o no anterior ao no a ser excluido
        while right:
            left = left.next
            right = right.next
        
        # excluir no apontando para o proximo
        left.next = left.next.next
        return dummy.next