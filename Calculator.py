import math as m
powr=0
value=0
print('Choose the Calculator:\n1.Basic\n2.Scientific')
selection=int(input())
if selection == 1:

    c=int(input('choose the operation:\n1.add\n2.sub\n3.div\n4.mult\n'))
    a=int(input('enter operand1:'))
    b=int(input('enter operand2:'))
    d={1:a+b,2:a-b,3:a/b,4:a*b}
    result=d[c]
    print('The result is:',result)
elif selection==2:
    print('Select the operation you want to perform:',
          '\n1.Sine',
          '\n2.Cosine',
          '\n3.Tangent',
          '\n4.Log',
          '\n5.Factorial',
          '\n6.SquareRoot',
          '\n7.Power',
          )
    choice=int(input())
    if choice == 7:
        print("Enter the value:")
        value=float(input())
        print("Enter the power:")
        powr=float(input())
    elif 0<choice<7:

        print("Enter the value:")
        value=float(input())

    operation = {
                 1:m.sin(value),
                 2:m.cos(value),
                 3:m.tan(value),
                 4:m.log(value),
                 5:m.factorial(int(value)),
                 6:m.sqrt(value),
                 7:m.pow(value,powr),
            }
    result = operation[choice]
    print("The result is:",result)
else:
    print("Wrong Input")