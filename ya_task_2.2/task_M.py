# Властелин Чисел: Братство общей цифры
# Во времена магии и драконов существовало мнение, что числа обладают великой силой,
# способной изменить мир.

# Всё началось с написания великих чисел. Три числа были переданы эльфам. 
# Семь — отданы повелителям гномов. А девять... были переданы человеческому роду.

# Но все они оказались обмануты, потому что существовало ещё одно число. 
# В стране Нумия на бумаге из тёмного папируса властелин Зерон тайно написал Единую Цифру, 
# подчиняющую себе все великие числа.

# Давайте выясним, что это за цифра.

# Формат ввода
# В первой строке записано двузначное число одного из эльфов.
# Во второй строке — Гномов.
# В третьей — Людей.

# Формат вывода
# Одна цифра — общая у всех трёх чисел в одинаковой позиции

# Пример 1
# Ввод
# 12
# 13
# 14

# Вывод
# 1

# Пример 2
# Ввод
# 23
# 13
# 63

# Вывод
# 3


# elf = str(input())
# gno = str(input())
# peo = str(input())

# elf_min = min(int(elf[0]), int(elf[1]))
# gno_min = min(int(gno[0]), int(gno[1]))
# peo_min = min(int(peo[0]), int(peo[1]))

# elf_max = max(int(elf[0]), int(elf[1]))
# gno_max = max(int(gno[0]), int(gno[1]))
# peo_max = max(int(peo[0]), int(peo[1]))

# same_num = 0
# if elf_min == gno_min or elf_min == gno_max:
#     if elf_min == peo_min or elf_min == peo_max:
#         same_num = elf_min
# elif elf_min == gno_max:
#     if elf_min == peo_max:
#         same_num = elf_min

# print(elf_min)
# print(elf_max)


elf = str(input())
gno = str(input())
peo = str(input())

elf_min = min(int(elf[0]), int(elf[1]))
gno_min = min(int(gno[0]), int(gno[1]))
peo_min = min(int(peo[0]), int(peo[1]))

elf_max = max(int(elf[0]), int(elf[1]))
gno_max = max(int(gno[0]), int(gno[1]))
peo_max = max(int(peo[0]), int(peo[1]))

if elf_min == gno_min:
    if elf_min == peo_min:
        print(elf_min)
    else:
        print(elf_max)
else:
    print(elf_max)