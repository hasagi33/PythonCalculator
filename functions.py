import math
import re
from operator import truediv


def operation(a, b, opp):
    match opp:
        case "+":
            return float(b) + float(a)
        case "-":
            return float(b) - float(a)
        case "*":
            if len(a) < 5 or len(b) < 5:
                return float(b) * float(a)
            else:
                return karatsuba(a, b)
        case "/":
            return float(b) / float(a)
        case "^":
            return pow(float(b), float(a))


def string_to_list(expression):
    return re.findall(r'[0-9.]+|[+\-*^/()]', expression)


def dot_position(decimal):
    dot_pos = decimal.rfind(".")
    return dot_pos


def karatsuba(a, b):
    # 22.545 2 5

    dot_pos_a = dot_position(a)
    dot_pos_b = dot_position(b)
    a.replace('.', '')
    b.replace('.', '')
    bonus_power = (len(a) - dot_pos_b) + (len(b) - dot_pos_a)
    shorter = 0
    longer = 0
    if len(a) > len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
    longer_log2 = math.log2(len(longer))
    longer_powered = longer.rjust(math.ceil(longer_log2), '0')
    shorter_powered = shorter.rjust(math.ceil(longer_log2), '0')

    result = recursive_karatsuba(longer_powered, shorter_powered)
    full_result = '.'.join([result[:(len(result) - bonus_power)], result[len(result) - bonus_power:]])
    return full_result


def recursive_karatsuba(x, y):
    # working on it
    if len(x) < 4 or len(y) < 4:
        return operation(x, y, "*")

    half = len(x) / 2
    x_left = x[:half]
    x_right = x[half:]
    y_left = y[:half]
    y_right = y[half:]

    z2 = recursive_karatsuba(x_left, y_left)
    z0 = recursive_karatsuba(x_right, y_right)
    z3 = recursive_karatsuba(string_add(x_left, x_right), string_add(y_left, y_right))
    z1 =

    return x * y


def string_add(a, b):
    result = ""
    carry = 0
    current_add = 0
    if len(b) > len(a):
        a = a.rjust(len(b), '0')
    elif len(a) < len(b):
        b = b.rjust(len(a), '0')
    for i in reversed(range(len(a))):
        current_add = int(a[i]) + int(b[i]) + carry
        if current_add > 9:
            carry = 1
            current_add = current_add[1:]
        result = ''.join([current_add, result])
    if current_add:
        result = ''.join([current_add, result])

    return result


def string_diff(a, b):
    # 124-098=26
    # 421-890 = - 6 ^1 - 3-1 ^1 1-1 = 620 || 026
    result = ""
    carry = 0
    first_is_bigger = first_bigger(a, b)
    if not first_is_bigger:
        a, b = b, a
    if len(b) > len(a):
        a = a.rjust(len(b), '0')
    elif len(a) < len(b):
        b = b.rjust(len(a), '0')



    return result


def remove_leading_zeroes(a):
    regexed = re.sub("^0+(?!$)", "", a)
    return regexed


def first_bigger(a, b):
    if len(a) < len(b):
        return False
    elif len(a) > len(b):
        return True
    for i in range(len(a)):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return True
