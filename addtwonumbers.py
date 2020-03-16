Source: https://leetcode.com/problems/add-two-numbers/
Author: Uditanshu

Question-
****************************************************
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*****************************************************

Solution-
*****************************************************
class Solution:
    
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=str(l1.val)
        b=str(l2.val) 
        next=l1.next
        while next:
            a=str(next.val)+a
            next=next.next
        next=l2.next
        while next:
            b=str(next.val)+b
            next=next.next
        c=str(int(a)+int(b))
        c=c[::-1]
       
        previousNode = None
        first = None
        for i in c:
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode  
        return first
********************************************************
