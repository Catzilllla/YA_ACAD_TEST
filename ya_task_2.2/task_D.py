# Список победителей
# Длинна трассы — 43872м, а зрители хотят узнать имя победителя.

# Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имена победителей в порядке занятых мест.

# Пример 1
# Ввод
# 10
# 5
# 7

# Вывод
# 1. Петя
# 2. Толя
# 3. Вася

# Пример 2
# Ввод
# 5
# 7
# 10

# Вывод
# 1. Толя
# 2. Вася
# 3. Петя


Petya = int(input())
Vasya = int(input())
Tolya = int(input())

name_pet = "Петя"
name_vas = "Вася"
name_tol = "Толя"

if Petya > Vasya and Petya > Tolya:
    if (Vasya > Tolya):
        top = name_pet
        middle = name_vas
        bottom = name_tol
    else:
        top = name_pet
        middle = name_tol
        bottom = name_vas
elif Vasya > Petya and Vasya > Tolya:
    if (Petya > Tolya):
        top = name_vas
        middle = name_pet
        bottom = name_tol
    else:
        top = name_vas
        middle = name_tol
        bottom = name_pet
else:
    if (Petya > Vasya):
        top = name_tol
        middle = name_pet
        bottom = name_vas
    else:
        top = name_tol
        middle = name_vas
        bottom = name_pet
    
print(f'1. {top}')
print(f'2. {middle}')
print(f'3. {bottom}')