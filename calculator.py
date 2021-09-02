def getNumber(x):
    while x:
        try:
            getArg = int(x)
        except ValueError:
            try:
                getArg = float(x)
            except ValueError:
                print('Incorrect type. Please, enter a number.')
                x = input()
            else:
                break
        else:
            break
    return getArg


x = getNumber(input())
while True:
    operation1 = input('Use +, -, *, /, ** or = for answer: ')
    while operation1 != '=':
        if operation1 == '+':
            y = getNumber(input())
            answer = x + y
        elif operation1 == '-':
            y = getNumber(input())
            answer = x - y
        elif operation1 == '*':
            y = getNumber(input())
            answer = x * y
        elif operation1 == '**':
            y = getNumber(input())
            answer = x ** y
        elif operation1 == '/':
            y = getNumber(input())
            if y != 0:
                answer = x / y
            else:
                print('Division by zero. Please, change the divisor')
                y = getNumber(input())
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
        x = getNumber(a)
        continue
