c='none'
while c!='0':
    a = int(input('Input the first number: '))
    b = int(input('Input the second number: '))
    c = input('Input the command(+, -, *, /, 0):  ')
    if c=='+':

        print('The sum is: ', a+b)
    elif c=='-':
        print('The difference is: ', a-b)

    elif c=='*':
        print('The multiplication is: ', a*b)

    elif c=='/':
        if b==0:
            print('Wrong input, try again')
            b=int(input('Input the second number: '))
            print('The devision is: ', a/b)
        else:
            print('The devision is: ', a/b)
