class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def createLinkedList(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])
result = addTwoNumbers(l1, l2)
printLinkedList(result) 

l1 = createLinkedList([0])
l2 = createLinkedList([0])
result = addTwoNumbers(l1, l2)
printLinkedList(result) 

l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = createLinkedList([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
printLinkedList(result) 
