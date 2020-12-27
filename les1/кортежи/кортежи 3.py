friends = ['Кирилл', 'Алмаз', 'Андрей', 'Александра', 'Петр']
popular_names = ['Александр', 'Данил', 'Михаил', 'Максим', 'Дмитрий', 'Иван', 'Матвей', 'Роман', 'Ольга', 'Анна']
for i in range (len(friends)):
    if friends[i] in popular_names:
        print(friends[i])