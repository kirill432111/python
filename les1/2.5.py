def Otvet(a1,b1,c1,a2,b2,c2):
    d=a1*b2-a2*b1
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    return x,y

a1,b1,c1,a2,b2,c2=map(int,input().split())
print(Otvet(a1,b1,c1,a2,b2,c2))
