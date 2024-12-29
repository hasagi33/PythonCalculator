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


    a=a.replace('.', '')
    b=b.replace('.', '')
    if dot_pos_b == -1:
        dot_pos_b = len(b)
    if dot_pos_a == -1:
        dot_pos_a = len(a)

    bonus_power = (len(a) - dot_pos_a) + (len(b) - dot_pos_b)

    if len(a) > len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
    longer_log2 = math.log2(len(longer))
    longer_powered = longer.rjust(pow(2,math.ceil(longer_log2)), '0')
    shorter_powered = shorter.rjust(pow(2,math.ceil(longer_log2)) , '0')


    result = recursive_karatsuba(longer_powered, shorter_powered)
    if bonus_power:
        full_result = '.'.join([result[:(len(result) - bonus_power)], result[len(result) - bonus_power:]])
    else:
        full_result = result
    return full_result


def recursive_karatsuba(x, y):
    if len(x) < 5 or len(y) < 5:
        return str(operation(x, y, "*"))

    half = int(len(x) / 2)

    x_left = x[:half]
    x_right = x[half:]
    y_left = y[:half]
    y_right = y[half:]


    z2 = recursive_karatsuba(x_left, y_left)
    z0 = recursive_karatsuba(x_right, y_right)
    z3 = recursive_karatsuba(string_add(x_left, x_right), string_add(y_left, y_right))

    z2=remove_leading_zeroes(z2.split(".")[0])
    z0=remove_leading_zeroes(z0.split(".")[0])
    z3=remove_leading_zeroes(z3.split(".")[0])

    z1 = string_diff(string_diff(z3,z2),z0).split(".")[0]

    z2=z2.ljust((len(z2)+half*2),'0')
    z1=z1.ljust((len(z1)+half),'0')

    result=string_add(string_add(z2,z1),z0)

    return result

def string_add(a, b):
    result = ""
    carry = 0
    a = a.rjust(len(b), '0')
    b = b.rjust(len(a), '0')
    for i in reversed(range(len(a))):
        current_add = int(a[i]) + int(b[i]) + carry
        carry=0
        # 54 + 66 =
        if current_add > 9:
            carry = 1
            current_add = current_add - 10
        result = ''.join([str(current_add), result])
    if carry:
        result = ''.join([str(carry), result])


    return result


def string_diff(a, b):
    result = ""
    carry = 0
    first_is_bigger = first_bigger(a, b)
    if not first_is_bigger:
        a, b = b, a
    a = a.rjust(len(b), '0')
    b = b.rjust(len(a), '0')


    for i in reversed(range(len(a))):
        opp=int(a[i])-carry-int(b[i])
        carry=0
        if opp<0:
            carry=1
            opp=10+opp
        result=''.join([str(opp),result])

    result=remove_leading_zeroes(result)
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
        if int(a[i]) > int(b[i]):
            return True
        elif int(a[i]) < int(b[i]):
            return False
    return True
