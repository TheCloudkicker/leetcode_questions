# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        print('l1', l1)
        print('l2', l2)
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            # Get val from Node and if no Node use 0
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # Add together
            sum = digit1 + digit2 + carry
            
            # Get mod value
            digit = sum % 10
            # Get Carry Value (i.e. for digits over 10)
            carry = sum // 10

            # Add val to new Node
            newNode = ListNode(digit)
            
            # Add new node to next 
            tail.next = newNode

            # Move To newNode that was just added to next
            tail = tail.next

            # move to next input nodes
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result