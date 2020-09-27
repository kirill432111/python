def sred(a=1,b=2,c=3):
    sr=(a+b+c)/3
    return sr

a,b,c=map(int, input('Введите 3 числа: ').split())
print(sred(a,b,c))
