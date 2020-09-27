def f(x):
    if x>=-2.4 and x<=5.7:
        y=x*x
    else:
        y=4
    return y
x=float(input('Введите x: '))
print('f=',f(x))
