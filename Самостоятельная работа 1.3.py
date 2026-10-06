# import random
#
# s1 = ['блистательно', 'неотразимо', 'восхитительно']
# s2 = ['прекрасна', 'мила', 'красива']
#
# print(f' Ты {random.choice(s1)} {random.choice(s2)}!')

# s = [x for x in range(10, 4, -1)]
#
# print(s)

words = ["море", "солнце", "майка", "отпуск"]

e_words = [i for i in words if i.startswith('e')]

print(e_words)

