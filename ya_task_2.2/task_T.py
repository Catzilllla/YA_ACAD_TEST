# Зайка — 2
# По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

# Формат ввода
# Три строки описывающих придорожную местность.

# Формат вывода
# Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.

# Пример 1
# Ввод
# березка елочка зайка волк березка
# сосна сосна сосна елочка грибочки медведь
# сосна сосна сосна белочка сосна белочка
# Вывод
# березка елочка зайка волк березка 33
# Пример 2
# Ввод
# зайка березка
# березка зайка
# березка елочка березка
# Вывод
# березка зайка 13


def print_zayka(str_1, str_2, str_3):
    symb_1 = len(str_1)
    symb_2 = len(str_2)
    symb_3 = len(str_3)


    if "зайка" in str_1:
        print(f'{str_1} {symb_1}')
    elif "зайка" in str_2:
        print(f'{str_2} {symb_2}')
    elif "зайка" in str_3:
        print(f'{str_3} {symb_3}')


str_1 = input()
str_2 = input()
str_3 = input()

len_str_1 = len(str_1)
len_str_2 = len(str_2)
len_str_3 = len(str_3)

print(len_str_1)
print(len_str_2)
print(len_str_3)

if (len_str_1 < len_str_2 and len_str_1 < len_str_3):
    print_zayka(str_1, str_2, str_3)

elif (len_str_2 < len_str_1 and len_str_2 < len_str_3):
    print_zayka(str_1, str_2, str_3)

elif (len_str_3 < len_str_2 and len_str_3 < len_str_1):
    print_zayka(str_1, str_2, str_3)
else:
    print_zayka(str_1, str_2, str_3)
