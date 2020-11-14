"""
LinkedList Cycle Length:
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# O(N) time | O(1) space
def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        # find cycle
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            # calculate length
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()

"""
We can use `find LinkedList Cycle` solution to find the cycle in the LinkedList.
Once the fast and slow pointers meet, we can save the slow pointer and
 iterate the whole cycle with another pointer until we see the slow pointer again
  to find the length of the cycle.
"""
