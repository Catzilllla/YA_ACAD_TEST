# Дед Мороз и конфеты
# Настало самое главное событие в детском саду — новогодний утренник.
# Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так, чтобы каждому досталось поровну. Напишите для робоняни алгоритм, который поможет распределить конфеты.

# Формат ввода
# В первой строке указано количество детей на утреннике.
# Во второй строке — количество конфет в конфетном отсеке робоняни.

# Формат вывода
# Сначала выведите количество конфет, которое выдано каждому ребенку, а затем количество конфет, что осталось в конфетном отсеке.

# Пример 1
# Ввод
# 3
# 100

# Вывод
# 33
# 1

# Пример 2
# Ввод
# 20
# 500

# Вывод
# 25
# 0


nnn = int(input())
mmm = int(input())

res = mmm % nnn
det = int(mmm / nnn)

print(det)
print(res)