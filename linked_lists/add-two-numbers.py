'''
## Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Solution:
    Doubly-linked list

    Time complexity: O(max(m,n)). Assume that mmm and nnn represents the
    length of l1 and l2 respectively, the algorithm above iterates at most
    max⁡(m,n) times.

    Space complexity : O(max⁡(m,n)). The length of the new list is at
    most max⁡(m,n)+1.
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def traverse_list(self):
        if self.head is None:
            return
        else:
            n = self.head
            while n is not None:
                print(n.val, " ")
                n = n.next


class Solution:

    def addTwoNumbers(self, l1=None, l2=None):
        dummyHead = ListNode(0)
        p, q = l1, l2
        curr = dummyHead
        carry = 0

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = carry + x + y
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

            if p:
                p = p.next
            if q:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    ll1 = ListNode(0)
    ll1.add_list_item(3)
    ll1.add_list_item(4)
    ll1.add_list_item(2)
    # ll1.traverse_list()

    ll2 = ListNode(0)
    ll2.add_list_item(4)
    ll2.add_list_item(6)
    ll2.add_list_item(5)
    # ll2.traverse_list()

    print(s.addTwoNumbers(ll1, ll2))
