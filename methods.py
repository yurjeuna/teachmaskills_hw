alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def check_if_number(x):
    while x:
        try:
            get_number = int(x)
            answer = 'True'
        except ValueError:
            try:
                get_number = float(x)
            except ValueError:
                if x == '0':
                    answer = 'True'
                elif x == '':
                    print("It's empty. Please, enter something.")
                    x = input()
                    continue
                else:
                    answer = 'False'
                break
        else:
            break
    return answer

def actions():
    action = input('Do you want to make the same with another one? (y/n) ')
    return action in ('y', 'Y')

def replacing(string, value1, value2, the_count):
    new_string = ''
    i = 0
    replacing_count = 0
    for i in range(len(string)):
        if string[i] == value1:
            while replacing_count < the_count:
                new_string += value2
                i += 1
                replacing_count += 1
                break
            else:
                new_string += string[i]
                i += 1
                continue
        else:
            new_string += string[i]
            i += 1
            continue

    return new_string

def uppercasing(string):
    new_string = []
    i = 0
    for i in range(len(string)):
        if string[i] in alphabet_low:
            letter_index = alphabet_low.index(string[i])
            new_string.append(alphabet_upp[letter_index])
            i += 1
            continue
        else:
            new_string.append(string[i])
            i += 1
            continue
    return  new_string

def lowercasing(string):
    new_string = []
    i = 0
    for i in range(len(string)):
        if string[i] in alphabet_upp:
            letter_index = alphabet_upp.index(string[i])
            new_string.append(alphabet_low[letter_index])
            i += 1
            continue
        else:
            new_string.append(string[i])
            i += 1
            continue
    return  new_string

def capitalizing(string, another_letters):
    new_string = []
    if string[0] in alphabet_low:
        letter_index = alphabet_low.index(string[0])
        new_string.append(alphabet_upp[letter_index])
    else:
        new_string.append(string[0])
    string2 = string[1:]
    if another_letters == '1':
        for i in range(len(string2)):
            new_string.append(string2[i])
            i += 1
            continue
    elif another_letters == '2':
        for i in range(len(string2)):
            if string2[i] in alphabet_upp:
                letter_index = alphabet_upp.index(string2[i])
                new_string.append(alphabet_low[letter_index])
                i += 1
                continue
            else:
                new_string.append(string2[i])
                i += 1
                continue
    return  new_string

def titling(string):
    new_string = []
    if string[0] in alphabet_low:
        letter_index = alphabet_low.index(string[0])
        new_string.append(alphabet_upp[letter_index])
        is_a_letter_before = True
    else:
        new_string.append(string[0])
        if new_string[0] in alphabet_low or new_string[0] in alphabet_upp:
            is_a_letter_before = True
        else:
            is_a_letter_before = False
    string2 = string[1:]
    for i in range(len(string2)):
        if is_a_letter_before == True:
            new_string.append(string2[i])
            if string2[i] in alphabet_low or string2[i] in alphabet_upp:
                is_a_letter_before = True
            else:
                is_a_letter_before = False
            i += 1
            continue
        elif is_a_letter_before == False:
            if string2[i] in alphabet_low:
                letter_index = alphabet_low.index(string2[i])
                new_string.append(alphabet_upp[letter_index])
                is_a_letter_before = True
                i += 1
                continue
            else:
                new_string.append(string2[i])
                if string2[i] in alphabet_low or string2[i] in alphabet_upp:
                    is_a_letter_before = True
                else:
                    is_a_letter_before = False
                i += 1
                continue
    return  new_string

def spliting(string, separator, maxsplit):
    new_string = []
    count = 0
    while count < maxsplit:
        if separator in string:
            my_index = string.index(separator)
            new_string.append(string[:my_index])
            string = string[(my_index + 1):]
            count += 1
            continue
        else:
            new_string.append(string[:])
            break
    else:
        new_string.append(string[:])
    return  new_string

def joining(a_list, delimiter):
    new_string = ''
    for i in range(len(a_list)):
        new_string += a_list[i]
        new_string += delimiter
        i += 1
    return  new_string

def print_if_digit():
    while True:
        number_check = input('Enter symbols for checking whether the string consists of digits only - ')
        answer = check_if_number(number_check)
        print(answer)
        if not actions():
            break
    return True

def print_replaces():
    while True:
        string_for_replacing = input('Enter a text for replacing symbols - ')
        oldvalue = input('What should we search for replace? ')
        newvalue = input('What should we replace it with? ')
        count = input('Enter a number specifying how many occurrences of the old value you want to replace. Default is all occurences. - ')
        if count == '':
            count = int(string_for_replacing.count(oldvalue))
        else:
            count = int(count)
        replaced_string = replacing(string_for_replacing, oldvalue, newvalue, count)
        print(replaced_string)
        if not actions():
            break
    return True

def print_all_letters_uppercase():
    while True:
        string_for_uppercasing = input('Enter a text for making all characters in upper case - ')
        uppercased_string = uppercasing(string_for_uppercasing)
        print(joining(uppercased_string, delimiter=''))
        if not actions():
            break
    return True

def print_all_letters_lowercase():
    while True:
        string_for_lowercasing = input('Enter a text for making all characters in lower case - ')
        lowercased_string = lowercasing(string_for_lowercasing)
        print(joining(lowercased_string, delimiter=''))
        if not actions():
            break
    return True

def print_first_uppercase():
    while True:
        string_for_capitalizing = input('Enter a text for converting the first character to uppercase - ')
        while True:
            another_letters_choice = input('If you want to leave the rest of the text unchanged, enter 1. \n'
                                    'If you want to reduce the rest of the text to lowercase, enter 2.')
            if another_letters_choice == '1' or another_letters_choice == '2':
                capitalized_string = capitalizing(string_for_capitalizing, another_letters_choice)
                print(joining(capitalized_string, delimiter=''))
                break
            else:
                print('Only 1 or 2.')
                continue
        if not actions():
            break
    return True

def print_first_of_all_words_uppercase():
    while True:
        string_for_titling = input('Enter a text for converting the first character of each word to uppercase. \n'
                                'If the word contains a number or a symbol, the first letter after thatwill be converted to upper case. - ')
        titled_string = titling(string_for_titling)
        print(''.join(titled_string))
        if not actions():
            break
    return True

def print_split():
    while True:
        string_for_spliting = input('Enter a text for spliting it into a list. - ')
        separator = input('Enter a separator for text spliting. By default any whitespace is a separator. - ')
        maxsplit = input('Enter, how many splits to do. By default it is all occurrences. - ')
        while True:
            if maxsplit == '':
                maxsplit = int(string_for_spliting.count(separator))
                break
            else:
                try:
                    maxsplit = int(maxsplit)
                    break
                except ValueError:
                    print("Enter a number or press 'enter'.")
                    continue
        if separator == '':
            separator = ' '
        else:
            separator = str(separator)
        splited_string = spliting(string_for_spliting, separator, maxsplit)
        print(splited_string)
        if not actions():
            break
    return True

def print_join():
    while True:
        string_for_joining = input("Enter a list for transformation it into a text. Use ' ' as separator. - ")
        delimiter = input('Enter a delimiter for list transformation. - ')
        list_for_joining = spliting(string_for_joining, separator = ' ', maxsplit = int(string_for_joining.count(' ')))
        joined_string = joining(list_for_joining, delimiter)
        print(joined_string)
        if not actions():
            break
    return True

def get_a_type(x):
    try:
        get_i = int(x)
        get_type = int
    except ValueError:
        if x == '0':
            get_i = int(x)
            get_type = int
        else:
            print('Incorrect type')
    return get_type

def ranging(list_for_ranging):
    start = 0
    step = 1
    stop = None
    ranged_list = []
    while True:
        if len(list_for_ranging) == 1:
            get_type0 = check_if_number(list_for_ranging[0])
            stop = get_type0(list_for_ranging[0])
            break
        elif len(list_for_ranging) == 2:
            get_type0 = get_a_type(list_for_ranging[0])
            start = get_type0(list_for_ranging[0])
            get_type1 = get_a_type(list_for_ranging[1])
            stop = get_type1(list_for_ranging[1])
            break
        elif len(list_for_ranging) == 3:
            get_type0 = get_a_type(list_for_ranging[0])
            start = get_type0(list_for_ranging[0])
            get_type1 = get_a_type(list_for_ranging[1])
            stop = get_type1(list_for_ranging[1])
            get_type2 = get_a_type(list_for_ranging[2])
            step = get_type2(list_for_ranging[2])
            break
        else:
            print('Enter up to 3 characters')
            continue

    if start < stop:
        i = start
        while i < stop:
            ranged_list.append(i)
            i += step
    else:
        i = start
        while i > stop:
            ranged_list.append(i)
            i -= (step * -1)
    return ranged_list

def print_range():
    while True:
        string_for_ranging = input('Enter data for genering number list - ')
        list_for_ranging = spliting(string_for_ranging, separator=' ', maxsplit = int(string_for_ranging.count(' ')) + 1)
        print(ranging(list_for_ranging))
        if not actions():
            break
    return True

def exit_from():
    exit()

menu_dict = {
    '1': print_if_digit,
    '2': print_replaces,
    '3': print_all_letters_uppercase,
    '4': print_all_letters_lowercase,
    '5': print_first_uppercase,
    '6': print_first_of_all_words_uppercase,
    '7': print_split,
    '8': print_join,
    '9': print_range,
    '0': exit_from
}

menu = """
\nChoice menu option:\n
1 - check some text is it valuable
2 - make some replaces in the text
3 - convert all letters in the text to uppercase
4 - convert all letters in the text to lowercase
5 - convert the first character of the text to uppercase
6 - convert the first character in each word to uppercase
7 - split some text into a list
8 - create some text from some objects (list)
9 - range a list with arithmetic sequence
0 - exit
"""

while True:
    menu_numb = input(menu)
    choice = menu_dict.get(menu_numb)
    if not choice:
        print("No entered option. Try again")
        continue
    choice()
