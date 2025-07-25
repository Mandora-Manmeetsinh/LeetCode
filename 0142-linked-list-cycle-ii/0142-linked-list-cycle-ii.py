# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow , fast = slow.next , fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head , slow = head.next , slow.next
        
        return head