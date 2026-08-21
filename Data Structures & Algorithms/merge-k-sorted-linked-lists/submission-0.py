# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            finalList = []

            # fazendo merge em pares de lista
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None # numero impar de listas
                finalList.append(self.mergeTwoLists(list1, list2)) # inserindo pares ordenados
            lists = finalList # atualizando lists parcialmente ordenado até len(lists) == 1
        return lists[0]
        

    def mergeTwoLists(self, list1, list2):
        # dummy armazena o inicio estatico da nova lista
        dummy = new_head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next

            new_head = new_head.next

        new_head.next = list1 or list2
        return dummy.next
        
        