# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def retrieveReverseSumFromListNode(listnode):
    """
    :type listnode: ListNode
    :rtype: int
    """
    digit = 1
    reverse_sum = 0
    while listnode != None:
        reverse_sum += listnode.val * digit
        digit = digit * 10
        listnode = listnode.next
    return reverse_sum

def createNewLinkedListFromNumber(number):
    """
    :type number
    :rtype: ListNode
    """
    string_number = str(number)
    elements_new_linked_list = list(reversed(string_number))

    new_linked_list = ListNode()
    current_node = new_linked_list
    for index, element in enumerate(elements_new_linked_list):
        current_node.val = int(element)

        if index != len(elements_new_linked_list) - 1:
            current_node.next = ListNode()
            current_node = current_node.next 

    return new_linked_list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retrieved_reverse_sum_number_from_l1 = retrieveReverseSumFromListNode(l1)
        retrieved_reverse_sum_number_from_l2 = retrieveReverseSumFromListNode(l2)

        sum_retrieved_reverse_numbers = retrieved_reverse_sum_number_from_l1 + retrieved_reverse_sum_number_from_l2

        new_linked_list_from_number = createNewLinkedListFromNumber(sum_retrieved_reverse_numbers)
        return new_linked_list_from_number
