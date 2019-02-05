class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head and head.next:
            firstValue = head.val
            secondValue = head.next.val
            head.val = secondValue
            head.next.val = firstValue
            head = head.next.next
        return result
