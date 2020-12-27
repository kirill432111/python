import math
def my_sin (x,n):
    x = x/180*math.pi
    q = x
    s = 0
    for i in range(1, n+1):
        s = s+ q
        q = q* (-1) * (x*x) / ((2*i+1) * (2*i))
    return s
def f(x):
    return 2.718281828459045**(1+x)
def tailor(x, eps):
    x = 1+x
    sum = 1+x
    term = x;
    n = 2;
    while term*term > eps*eps:
        term *= x/n
        n += 1
        sum += term
    return sum

a=3.0
b=4.0
krok=(b-a)/10

while a<=b:
    print(round(a,2), end=' ')
    print(round(f(a),5),end=' ')
    print(round(tailor(a,1e-6),5))
    a+=krok