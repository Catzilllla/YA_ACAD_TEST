# Кто быстрее на этот раз?
# Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.

# На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имя победителя гонки.

# Примечание
# Гарантируется, что победителем стал только один.

# Пример 1
# Ввод
# 10
# 5
# 7
# Вывод
# Петя
# Пример 2
# Ввод
# 5
# 7
# 10
# Вывод
# Толя

Petya = int(input())
Vasya = int(input())
Tolya = int(input())

if Petya > Vasya and Petya > Tolya:
    print("Петя")
elif Vasya > Petya and Vasya > Tolya:
    print("Вася")
elif Tolya > Petya and Tolya > Vasya:
    print("Толя")