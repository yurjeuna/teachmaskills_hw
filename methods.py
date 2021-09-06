alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def check_if_number(x):
    while x:
        try:
            get_number = int(x)
            answer = True
        except ValueError:
            if x == '0':
                answer = True
            elif x == '':
                print("It's empty. Please, enter something.")
                x = input()
                continue
            else:
                answer = False
                break
        else:
            break
    return answer


def replacing(string, value1, value2, the_count):
    new_string = []
    i = 0
    replacing_count = 0
    for i in range(len(string)):
        if string[i] == value1:
            while replacing_count < the_count:
                new_string.append(value2)
                i += 1
                replacing_count += 1
                break
            else:
                new_string.append(string[i])
                i += 1
                continue
        else:
            new_string.append(string[i])
            i += 1
            continue
    return  new_string


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

choice = input('If you want to check some text is it valuable, print 1. \n'
                'If you want to make some replaces in the text, print 2. \n'
                'If you want to convert all letters in the text to uppercase, print 3. \n'
                'If you want to convert all letters in the text to lowercase, print 4. \n'
                'If you want to convert the first character of the text to uppercase, print 5. \n'
                'If you want to convert the first character in each word to uppercase, print 6. \n'
                'If you want to split some text into a list, print 7. \n'
                'If you want to create some text from some objects, print 8. \nSo your choice is - ')
while choice:
    if choice == '1':
        while choice:
            number_check = input('Enter symbols for checking whether the string consists of digits only - ')
            answer = check_if_number(number_check)
            print(answer)
            action1 = input('If you want to check another symbols, print 1. If you want to choose another method, print 2. ')
            if action1 == '1':
                continue
            else:
                break
    elif choice == '2':
        while choice:
            string_for_replacing = input('Enter a text for replacing symbols - ')
            oldvalue = input('What should we search for replace? ')
            newvalue = input('What should we replace it with? ')
            count = input('Enter a number specifying how many occurrences of the old value you want to replace. Default is all occurences. - ')
            if count == '':
                count = int(string_for_replacing.count(oldvalue))
            else:
                count = int(count)
            replaced_string = replacing (string_for_replacing, oldvalue, newvalue, count)
            print(replaced_string)
            action2 = input('If you want to make replaces with another text, print 1. If you want to choose another method, print 2. ')
            if action2 == '1':
                continue
            else:
                break
    elif choice == '3':
        while choice:
            string_for_uppercasing = input('Enter a text for making all characters in upper case - ')
            uppercased_string = uppercasing(string_for_uppercasing)
            print(''.join(uppercased_string))
            action3 = input('If you want to make all characters in upper case with another text, print 1. If you want to choose another method, print 2. ')
            if action3 == '1':
                continue
            else:
                break
    elif choice == '4':
        while choice:
            string_for_lowercasing = input('Enter a text for making all characters in lower case - ')
            lowercased_string = lowercasing(string_for_lowercasing)
            print(''.join(lowercased_string))
            action4 = input('If you want to make all characters in lower case with another text, print 1. If you want to choose another method, print 2. ')
            if action4 == '1':
                continue
            else:
                break
    elif choice == '5':
        while choice:
            string_for_capitalizing = input('Enter a text for converting the first character to uppercase - ')
            another_letters_choise = input('If you want to leave the rest of the text unchanged, enter 1. \n'
                               'If you want to reduce the rest of the text to lowercase, enter 2.')
            if another_letters_choise != '1' or another_letters_choise != '2':
                print('Only 1 or 2.')
                continue
            else:
                capitalized_string = capitalizing(string_for_capitalizing, another_letters_choise)
                print(''.join(capitalized_string))
                action5 = input('If you want to convert the first character to uppercase in another text, print 1. If you want to choose another method, print 2. ')
                if action5 == '1':
                    continue
                else:
                    break
    elif choice == '6':
        while choice:
            string_for_titling = input('Enter a text for converting the first character of each word to uppercase. \n'
                                   'If the word contains a number or a symbol, the first letter after thatwill be converted to upper case. - ')
            titled_string = titling(string_for_titling)
            print(''.join(titled_string))
            action6 = input('If you want to convert the first character of each word to uppercase in another text, print 1. \n'
                            'If you want to choose another method, print 2. ')
            if action6 == '1':
                continue
            else:
                break
    elif choice == '7':
        while choice:
            string_for_spliting = input('Enter a text for spliting it into a list. - ')
            separator = input('Enter  separator for splitting the text. By default any whitespace is a separator. - ')
            maxsplit = input('Enter, how many splits to do. By default it is all occurrences. - ')
            if maxsplit == '':
                maxsplit = int(string_for_spliting.count(separator))
            else:
                try:
                maxsplit = int(maxsplit)
                except ValueError:
                    print("Enter a number or press 'enter'.")
                    continue
            if separator == '':
                separator = ' '
            else:
                separator = str(separator)
            splited_string = spliting(string_for_spliting, separator, maxsplit)
            print(splited_string)
            action7 = input('If you want to split another text, print 1. If you want to choose another method, print 2. ')
            if action7 == '1':
                continue
            else:
                break
    else:
        break
        
