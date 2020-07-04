# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextVal=None):
        self.val = val
        self.nextVal = nextVal
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.nextVal: return head
        cont = 1
        list_nodes = head
        while list_nodes.nextVal:
            cont += 1
            list_nodes = list_nodes.nextVal

        middle = int(cont/2) + 1
        cont = 1
        while head.nextVal:
            cont += 1
            head = head.nextVal
            if cont == middle:
                return head
