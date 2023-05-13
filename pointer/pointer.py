import random as rd

class ListNode:
    value: int
    next = None
    def __init__(self, value):
        self.value = value

def traverse(ListNode):
    
    print(ListNode.value)
    if ListNode.next:
        traverse(ListNode.next)

def add_node(node):
    node.next = ListNode(rd.randint(1, 20))
    return node.next


if __name__ == "__main__":

    # build a linkedlist that has cycle 
    node = ListNode(1)
    new_node = add_node(node)
    for i in range(25):
        new_node = add_node(new_node)
    new_node.next = node.next.next.next.next.next

    # use slow & fast pointer to get start, len of cycle
    slow = node
    fast = node
    step = 0

    # cycle length
    while True:
        slow = slow.next
        fast = fast.next.next
        step += 1
        if slow == fast:
            print("has cycle")
            print(f"length: {step}")
            break
    
    # cycle start at
    slow = node
    step = 0
    while True:
        slow = slow.next
        fast = fast.next        
        step += 1
        if slow == fast:
            print(f"start at {step}")
            break
        



    # traverse(node)