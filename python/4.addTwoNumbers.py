'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbersBF(l1, l2):
    def to_number(node):
        num = 0
        place = 1
        while node:
            num += node.val * place
            place *= 10
            node = node.next
        return num

    num1 = to_number(l1)
    num2 = to_number(l2)
    total = num1 + num2
    if total == 0:
        return ListNode(0)

    dummy = ListNode()
    current = dummy

    while total > 0:
        digit = total % 10
        current.next = ListNode(digit)
        current = current.next
        total //= 10

    return dummy.next



def addTwoNumbersST(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next