"""
LinkedList Cycle
Given the head of a Singly LinkedList,
write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    fast = head
    slow = head
    while fast != None:
        if fast == slow and fast != head:
            return True
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    return False


def has_cycle2(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # found the cycle
    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList has cycle: " + str(has_cycle2(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList has cycle: " + str(has_cycle2(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()

"""
SOLUTION:
Imagine two racers running in a circular racing track. 
If one racer is faster than the other, the faster racer is bound to catch up and cross the slower racer from behind.
We can use this fact to devise an algorithm to determine if a LinkedList has a cycle in it or not.

Imagine we have a slow and a fast pointer to traverse the LinkedList.
In each iteration, the slow pointer moves one step and the fast pointer moves two steps. 
This gives us two conclusions:

    1. If the LinkedList doesn’t have a cycle in it, the fast pointer will reach the end of the LinkedList
        before the slow pointer to reveal that there is no cycle in the LinkedList.
    2.The slow pointer will never be able to catch up to the fast pointer if there is no cycle in the LinkedList.

If the LinkedList has a cycle, the fast pointer enters the cycle first, followed by the slow pointer. 
After this, both pointers will keep moving in the cycle infinitely. 
If at any stage both of these pointers meet, we can conclude that the LinkedList has a cycle in it. 
Let’s analyze if it is possible for the two pointers to meet. 
When the fast pointer is approaching the slow pointer from behind we have two possibilities:
    1.The fast pointer is one step behind the slow pointer.
    2.The fast pointer is two steps behind the slow pointer.
All other distances between the fast and slow pointers will reduce to one of these two possibilities.

NOTE:
Let’s analyze these scenarios, considering the fast pointer always moves first:
    1. If the fast pointer is one step behind the slow pointer: 
        The fast pointer moves two steps and the slow pointer moves one step, and they both meet.
    2. If the fast pointer is two steps behind the slow pointer: 
        The fast pointer moves two steps and the slow pointer moves one step. 
        After the moves, the fast pointer will be one step behind the slow pointer, which reduces this scenario to the first scenario. 
        This means that the two pointers will meet in the next iteration.

This concludes that the two pointers will definitely meet if the LinkedList has a cycle.
A similar analysis can be done where the slow pointer moves first.
"""
