def check_if_number(x):
    while x:
        try:
            get_number = int(x)
        except ValueError:
            try:
                get_number = float(x)
            except ValueError:
                if x == '0':
                    get_number = int(0)
                elif x == '':
                    print("It's empty. Please, enter something.")
                    x = input()
                    continue
                else:
                    print('Incorrect type. Please, enter a number.')
                    x = input()
                    continue
            else:
                break
        else:
            break
    return get_number


x = check_if_number(input())
while True:
    operation1 = input('Use +, -, *, /, ** or = for answer: ')
    while operation1 != '=':
        if operation1 == '+':
            y = check_if_number(input())
            answer = x + y
        elif operation1 == '-':
            y = check_if_number(input())
            answer = x - y
        elif operation1 == '*':
            y = check_if_number(input())
            answer = x * y
        elif operation1 == '**':
            y = check_if_number(input())
            answer = x ** y
        elif operation1 == '/':
            y = check_if_number(input())
            if y != 0:
                answer = x / y
            else:
                print('Division by zero. Please, change the divisor')
                y = check_if_number(input())
                answer = x / y
        else:
            print('Incorrect operation. Please, try again.')
            operation1 = input()
            continue
        x = answer
        operation1 = input()
    print(x, 'If you want to continue with new number, please, enter it. '
             'Print x if you want to continue with this number. Or press s if you want to stop.')
    a = input()
    if a == 'x' or a == 'X':
        continue
    elif a == 's' or a == 'S':
        break
    else:
        x = check_if_number(a)
        continue
        
