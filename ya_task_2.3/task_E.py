# Внимание! Акция!
# В продуктовом магазине объявили акцию:
# «На все товары с ценой не менее 500 тугриков предоставляется скидка 10%».

# Нас попросили разработать программное обеспечение кассового автомата, 
# которое будет считать итоговую сумму покупки с учётом скидки.

# Формат ввода
# Вводится некоторое количество рациональных чисел — стоимость товаров.
# Список завершается значением 0.

# Формат вывода
# Требуется вывести сумму всех товаров с учётом объявленной акции.

# Пример 1
# Ввод
# 100
# 500
# 333
# 0

# Вывод
# 883.0

# Пример 2
# Ввод
# 512
# 499
# 342.50
# 0

# Вывод
# 1302.3

end_input = float(input())
end = "0"
goods = 0
while end_input != end:
    if float(end_input) >= 500:
        goods = float(goods) + float(end_input) - float(float(end_input) / 10)
    else:
        goods = float(goods) + float(end_input)

    end_input = input()

print(goods)
