# Интересное сложение
# Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
# И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда.
# Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.

# Формат ввода
# В первой и второй строках записаны натуральные числа меньше 1000.

# Формат вывода
# Одно число — результат сложения введённых чисел без учёта переносов.

# Пример 1
# Ввод
# 123
# 99

# Вывод
# 112

# Пример 2
# Ввод
# 405
# 839

# Вывод
# 234


a = int(input())
b = int(input())
sum = 0

s1_num1_end = int(a % 10)
s2_num1_end = int(b % 10)

s1_num2_end = int((a / 10) % 10)
s2_num2_end = int((b / 10) % 10)

s1_num3_end = int(a / 100)
s2_num3_end = int(b / 100)


sum_1 = int((s1_num3_end + s2_num3_end) % 10)
sum_2 = int((s1_num2_end + s2_num2_end) % 10)
sum_3 = int((s1_num1_end + s2_num1_end) % 10)

print(f"{sum_1}{sum_2}{sum_3}")