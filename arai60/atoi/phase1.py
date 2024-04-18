INT_MAX = 2 ** 31 -1
INT_MIN = - 2 ** 31
# 仮に数字の場合文字列の最初に来うるのは符号か数字のみ
# 符号が来た場合も次の文字が数字じゃなければならない
# is_number -> extract_number(integer部分を抜き取る) -> 数字化処理

def char_is_number(char: str)->bool:
    if ord(char) >= ord("0") and ord("9") >= ord(char):
        return True
    return False

def is_number(s: str)->bool:
    for index, char in enumerate(s):
        if char == " ":
            continue
        elif char == "-" or char == "+":
            if index == len(s) - 1:
                #符号が終端の場合
                return False
            else:
                #次の文字が数字かどうかで判断
                return char_is_number(s[index+1])
        elif char_is_number(char):
            return True
        else:
            return False
    return False

def search_start_index(s: str)->int:
    for index, char in enumerate(s):
        if char == "+" or char == "-":
            return index
        elif char_is_number(char):
            return index

def extract_number(s: str)->str:
    start_index = search_start_index(s)
    end_index = len(s)
    for index in range(start_index+1, len(s)):
        if not char_is_number(s[index]):
            end_index = index
            break
    return s[start_index:end_index]

def string_to_integer(s: str)->int:
    if not is_number(s):
        return 0

    extracted_number_string = extract_number(s)
    sign = 1
    if extracted_number_string[0] == "-":
        sign = -1
        extracted_number_string = extracted_number_string[1:]
    elif extracted_number_string[0] == "+":
        extracted_number_string = extracted_number_string[1:]
    
    after_atoi_number = 0
    for index, char in enumerate(extracted_number_string):
        digit = len(extracted_number_string) - index - 1
        after_atoi_number += (ord(char)-ord("0")) * 10 ** digit
    
    return after_atoi_number * sign
    


def clamp(number: int) -> int:
    if number > INT_MAX:
        return INT_MAX
    elif number < INT_MIN:
        return INT_MIN
    return number


print(string_to_integer("3.141590"))
print(string_to_integer("   -42"))
print(string_to_integer("+1"))
print(string_to_integer("00000-42a1234"))