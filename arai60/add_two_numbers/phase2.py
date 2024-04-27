# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def retrieveReverseNumber(listnode):
    digit = 1
    reverse_number = 0
    while listnode != None:
        reverse_number += listnode.val * digit
        digit = digit * 10 # shift a digit
        listnode = listnode.next # go to next node
    return reverse_number

def createNewReverseLinkedListFromNumber(number):
    new_reverse_linked_list = ListNode()
    current_node = new_reverse_linked_list # shallow copy
    string_num = str(number)
    new_reverse_linked_list_elements = list(reversed(string_num)) # ex. "123" -> ["3", "2", "1"]
    for index, number in enumerate(new_reverse_linked_list_elements):
        current_node.val = int(number)

        if index != len(new_reverse_linked_list_elements) - 1:
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