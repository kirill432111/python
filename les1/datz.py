print("введите кол-во игр:  ")
x=int(input())

for i in range(x):
    print("введите кол-во секторов и номер черной мишени:  ")
    max = -9999
    n,k=map(int,input().split())
    print("введите значения секторов: ")
    a = list(map(int, input().split()))



    if len(a)!=n:
        print('введите верное кол-во секторов')
    else:
        if (k == -1):
            for i in range(n):
                s = 0
                for j in range(n):
                    b = i + j
                    if b > n - 1:
                        b = b - n
                    s = s + a[b]
                    if s > max:
                        max = s
            print(max)
        else:
            a[k] = min(a)
            if a[k] > 0:
                a[k] = 0
            for i in range(n):
                s = 0
                for j in range(n):
                    b = i + j
                    if b > n - 1:
                        b = b - n
                    s = s + a[b]
                    if s > max:
                        max = s
            print(max)