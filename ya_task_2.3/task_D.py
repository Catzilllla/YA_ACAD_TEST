# Считалочка 2.0
# Дети продолжают запоминать цифры, а мы им помогать.
# Нам вновь называют начало и конец последовательности чисел, а мы выводим их и числа между.

# Формат ввода
# Два числа, каждое с новой строки.

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
# 3
# -3

# Вывод
# 3 2 1 0 -1 -2 -3


num_first = int(input())
num_secon = int(input())
stroka = ""

if num_first < num_secon:
    for index in range(num_first, num_secon + 1):
        stroka = stroka + str(index) + " "
else:
    for index in range(num_first, num_secon - 1, -1):
        stroka = stroka + str(index) + " "

print(stroka)
