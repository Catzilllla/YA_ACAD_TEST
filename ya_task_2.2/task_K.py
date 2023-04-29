# Красота спасёт мир
# Одно из древних поверий гласит, что трёхзначное число красиво, 
# если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

# Напишите систему определяющую красоту числа.

# Формат ввода
# Одно трёхзначное число

# Формат вывода
# YES — если число красивое, иначе — NO

# Пример 1
# Ввод
# 123

# Вывод
# YES

# Пример 2
# Ввод
# 748

# Вывод
# NO


number = input()
min_num = min(int(number[0]), int(number[1]), int(number[2]))
max_num = max(int(number[0]), int(number[1]), int(number[2]))
# print(f'max = {max_num}')
# print(f'min = {min_num}')

if int(number[0]) != min_num and int(number[0]) != max_num:
    middle = number[0]
elif int(number[1]) != min_num and int(number[1]) != max_num:
    middle = number[1]
else:
    middle = number[2]

# print(f'middle = {middle}')
n_mid = int(middle) * 2
n_sum = int(min_num) + int(max_num)

if n_mid == n_sum:
    print("YES")
else:
    print("NO")
