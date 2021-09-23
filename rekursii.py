import string


def palindrom(string1):
    a = string1.lower()
    for i in set(a).intersection(set(string.punctuation)):
        a = a.replace(i, '')
    a = ''.join(a.split(' '))
    re_a = a[::-1]
    return a == re_a

def numb_of_negatives(my_list):
    count = 0
    if my_list[count] < 0:
        count = 1
    if len(my_list) - 1 == 0:
        return count
    else:
        return count + numb_of_negatives(my_list = my_list[1:])

def sum_of_numbers(my_list, sum1 = None):
    if sum1 is None:
        sum1 = 0
    sum1 += my_list[0]
    if len(my_list) - 1 > 0:
        my_list = my_list[1:]
        return sum_of_numbers(my_list, sum1)
    else:
        return sum1

def is_prime(numb, divis = None):
    if divis is None:
        divis = numb - 1
    if numb >= 2:
        while divis >= 2:
            if numb % divis == 0:
                return False
            return is_prime(numb, divis= divis - 1)
        return True
    return False

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * power(x, y= y - 1)

def to_binary(n, numb = None):
    if numb is None:
        numb = []
    if n == 1:
        numb.append(1)
        numb.reverse()
        return ''.join(map(str, numb))
    elif n == 2:
        numb.append(0)
        n = 1
        return to_binary(n, numb)
    while n > 2:
        numb.append(n % 2)
        n = n // 2
        return to_binary(n, numb)

def from_binary(n, new_n = None):
    if new_n is None:
        new_n = 0
    if n[0] == '1':
        new_n += 2 ** (len(n) - 1)
    if len(n) - 1 > 0:
        n = n[1:]
        return from_binary(n, new_n)
    else:
        return new_n
