# _*_ coding: utf-8 _*_
__author__ = "bobo"
__date__ = "2019/10/20 19:16"

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        if head.next is None:
            return head

        # 迭代法
        # node = None
        # while head:
        #     next = head.next
        #     head.next = node
        #     node = head
        #     head = next
        # return node
        return self.helper(head, None)

    # 递归法
    def helper(self, head, new_link):
        if not head:
            return new_link
        temp = head.next
        head.next = new_link
        return self.helper(temp, head)
