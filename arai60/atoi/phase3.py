INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31
def char_is_number(char: str)->int:
    if ord(char) >= ord("0") and ord("9") >= ord(char):
        return True
    return False

def string_to_integer(s: str)->int:
    if len(s) == 0:
        return 0

    current_pointer = 0
    while current_pointer < len(s):
        if s[current_pointer] != " ":
            break
        current_pointer += 1

    if current_pointer == len(s):
        return 0
    
    sign = 1
    # 符号処理
    if s[current_pointer] == "+":
        current_pointer += 1
    elif s[current_pointer] == "-":
        sign = -1
        current_pointer += 1
    
    abs_value = 0
    while current_pointer < len(s) and char_is_number(s[current_pointer]):
        abs_value *= 10
        abs_value += ord(s[current_pointer]) - ord("0")
        if abs_value * sign > INT_MAX:
            return INT_MAX
        elif abs_value * sign < INT_MIN:
            return INT_MIN
        current_pointer += 1

    return abs_value * sign

class Solution:
    def myAtoi(self, s: str) -> int:
        after_atoi_number = string_to_integer(s)
        return after_atoi_number