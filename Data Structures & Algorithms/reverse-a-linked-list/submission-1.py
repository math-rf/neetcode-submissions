# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr != None:
            # nó apos head
            temp = curr.next
            # ponteiro de proximo aponta para o anterior
            curr.next = prev
            # anterior do proximo é o atual
            prev = curr
            # atual é o proximo (recursao)
            curr = temp
        # retorna ponteiro do ultimo elemento que aponta para anterior etc
        return prev
