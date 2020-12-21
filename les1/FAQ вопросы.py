###########  1 ВОПРОС
mas = [i for i in range(100)]
del mas[50]
for k in range(len(mas) - 1):
    if mas[k + 1] - mas[k] > 1:
        print(mas[k + 1] - 1)


###########  2 ВОПРОС
mas=[i for i in range(10)]
mas.append(5)

mas.sort()
for i in range(len(mas)-1):
    if mas[i]==mas[i+1]:
        print(mas[i])


###########  3 ВОПРОС
a=[1,2,3,7,8,12,45,96,56]
print(max(a))
print(min(a))


###########  4 ВОПРОС
def find_pars(L,summ):
    s = set(L)
    edgeCase = summ/2
    if L.count(edgeCase) ==2:
        print (edgeCase, edgeCase)
    s.remove(edgeCase)
    for i in s:
        diff = summ-i
        if diff in s:
            print (i, diff)

L = [1,2,3,11,7,9,5,8]
summ = 10
find_pars(L,summ)



###########  5 ВОПРОС
x=[8,1,8,2,7,3,8,4,5,7,7]
povt=[item for item in set(x) if x.count(item)>1]
print(povt)



###########  6 ВОПРОС
a=[1,2,3,3,4,5,3,6]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)


###########  7 ВОПРОС
x = [1, 5, 3, 7, 4, 5]
import random


def quicksort(x):
    if len(x) <= 1:
        return x
    else:
        q = random.choice(x)
    l_x = [n for n in x if n < q]

    e_x = [q] * x.count(q)
    b_x = [n for n in x if n > q]
    return quicksort(l_x) + e_nums + quicksort(b_x)


print(quicksort(x))


########### 8 ВОПРОС
a=[1,2,3,4,2,3,6]
S=set()
M=[]
for i in a:
    if i not in S:
        S.add(i)
        M.append(i)
print(M)


###########  9 ВОПРОС
a=[1,2,3,4,5,6]
#first var
for i in reversed(a):
    print(i)
#second var
print(a[::-1])



###########  10 ВОПРОС
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
seq=[1,2,3,4,2,3,5,6]
print(f7(seq))

