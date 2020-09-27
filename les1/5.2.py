def max(a,b):
    if a>b :
        m=a

    if b>a:
        m=b
    return m

a,b=map(int,input('Введите 2 числа: ').split())
print('Максимальное число: ',max(a,b))
