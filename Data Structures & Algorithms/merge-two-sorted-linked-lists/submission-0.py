# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = None #set to list 1 or list 2 as start
        prev = None
        if list1.val < list2.val:
            head = list1
            prev = list1
            list1 = list1.next
        else:
            head = list2
            prev = list2
            list2 = list2.next

        while list1 and list2 is not None:
            if list1.val < list2.val:
                nxt = list1.next
                prev.next = list1
                prev = list1
                list1 = nxt
            else:
                nxt = list2.next
                prev.next = list2
                prev = list2
                list2 = nxt
        
        if list1 is not None:
            prev.next = list1
        
        if list2 is not None:
            prev.next = list2
        
        return head








