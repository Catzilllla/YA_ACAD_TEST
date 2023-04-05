# Доставка
# Продуктовый склад и магазин находятся на одной дороге города Н.
# Склад находится на отметке AA км, а магазин — BB км. Средняя скорость автомобиля, доставляющего товары, CC км/ч.
# За какое время продукты попадают со склада в магазин?

# Формат ввода
# Три натуральных числа AA, BB и CC, каждое на отдельной строке.

# Формат вывода
# Одно рациональное число с точностью до сотых.

# Пример 1
# Ввод
# 10
# 32
# 5

# Вывод
# 4.40

# Пример 2
# Ввод
# 1
# 100
# 30

# Вывод
# 3.30


A = int(input())
B = int(input())
C = int(input())

T = float((B - A) / C)

print(T)