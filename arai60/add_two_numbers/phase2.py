# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def retrieveReverseNumber(listnode):
    order = 1
    reverse_number = 0
    while listnode != None:
        reverse_number += listnode.val * order
        order = order * 10 # shift a digit
        listnode = listnode.next # go to next node
    return reverse_number

def createNewReverseLinkedListFromNumber(number):
    new_reverse_linked_list = ListNode()
    current_node = new_reverse_linked_list # shallow copy
    string_num = str(number)
    for index in range(len(string_num)):
        current_node.val = int(string_num[-index-1])

        if index != len(string_num) - 1:
            current_node.next = ListNode()
            current_node = current_node.next
    return new_reverse_linked_list


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retrieved_number_from_l1 = retrieveReverseNumber(l1)
        retrieved_number_from_l2 = retrieveReverseNumber(l2)

        sum_retrieved_numbers = retrieved_number_from_l1 + retrieved_number_from_l2
        
        new_reverse_linked_list = createNewReverseLinkedListFromNumber(sum_retrieved_numbers)

        return new_reverse_linked_list