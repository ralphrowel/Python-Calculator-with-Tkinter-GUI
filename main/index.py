while True:
    numbers = []
    while True:
        value = input('enter a numbers or type "done" if its done: ')
        if value == "done":
            break
        numbers.append(int(value))
        
    c = str(input('choose whic operator will you use "+", "-", "x": '))

    def addition(): 
        result = sum(numbers)
        print(result)

    def subtraction():
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        print(result)

    def multiplication():
        result = 1
        for n in numbers:
            result *= n
        print(result)

    if c == "+":
        addition()
    elif c == "-":
        subtraction()
    elif c == "x":
        multiplication()
    else:
        print('sorry we didnt get that try again')

    loop = str(input('would you like to try again "yes" or "no" '))

    if loop == "yes":
        print('ok!')
    elif loop == "no":
        print('byebye')
        break
    else:
        print('sorry we didint get that')