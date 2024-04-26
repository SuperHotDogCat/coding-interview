INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31

def char_is_number(c: str)->bool:
    return ord("0") <= ord(c) <= ord("9")

class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        
        if index == len(s):
            return 0
        
        sign = 1
        if s[index] == "+":
            index += 1
        elif s[index] == "-":
            sign = -1
            index += 1
        
        absolute_value = 0
        while index < len(s) and char_is_number(s[index]):
            absolute_value *= 10
            absolute_value += ord(s[index]) - ord("0")
            if absolute_value * sign > INT_MAX:
                return INT_MAX
            elif absolute_value * sign < INT_MIN:
                return INT_MIN
            index += 1

        return absolute_value * sign
        