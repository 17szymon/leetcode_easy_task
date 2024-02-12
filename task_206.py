from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_list = []

        while node:
            new_list.insert(0, node.val)
            node = node.next

        head = None
        for val in new_list:
            new_node = ListNode(val)
            if not head:
                head = new_node
            else:
                current = head
                while current.next:
                    current = current.next
                current.next = new_node

        return head


solution = Solution()

result = solution.reverseList(head)
while result:
    print(result.val)
    result = result.next
