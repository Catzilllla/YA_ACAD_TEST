# Считалочка
# Ребята в детском саду учат числа, и мы можем им в этом помочь.
# Ребята дают нам два числа — начало и конец последовательности чисел.
# Наша задача вывести все числа от начала до конца, заполнив промежуток между ними.

# Формат ввода
# Два числа в порядке возрастания, каждое с новой строки.

# Формат вывода
# Все числа от начала до конца (включительно), записанные через пробел.

# Пример 1
# Ввод
# 1
# 10

# Вывод
# 1 2 3 4 5 6 7 8 9 10

# Пример 2
# Ввод
# -3
# 3

# Вывод
# -3 -2 -1 0 1 2 3


num_first = int(input())
num_secon = int(input())
stroka = ""

for index in range(num_first, num_secon + 1):
    stroka = stroka + str(index) + " "

print(stroka)
