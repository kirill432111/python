count=0
anagram=['тропа', "торг", "апорт", "грот", "жизнь", "учеба", "смерть"]
for i in anagram:
    for j in anagram:
        if i==j[::-1]:
            print("Анаграмма встречающаяся в списке слов: ",i)