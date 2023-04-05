# Первому игроку приготовиться
# Во многих играх порядок определяется броском кубика или монетки, — а в нашей первым ходит тот, 
# чьё имя лексикографически меньше.

# Определите, кто из игроков будет ходить первым.

# Формат ввода
# Три имени игроков, каждое из которых записано с новой строки.

# Формат вывода
# Имя игрока, который будет ходить первым.

# Пример 1
# Ввод
# Вова
# Аня
# Боря

# Вывод
# Аня

# Пример 2
# Ввод
# Толя
# Коля
# Вася

# Вывод
# Вася


def ascii_name(name_t):
    sum_t = 0
    for ind in name_t:
        sum_t = sum_t + ord(ind)
    
    # print(f"summa \"{name_t}\" = {sum_t}")

def compare_ascii_name(sum_1, sum_2, sum_3):
    if (sum_1 < sum_2):
        if(sum_1 < sum_3):
            return name_1
        
    elif (sum_2 < sum_1):
        if(sum_2 < sum_3):
            return name_2
        
    elif (sum_3 < sum_1):
        if(sum_3 < sum_2):
            return name_3


name_1 = input()
name_2 = input()
name_3 = input()

summa_1 = ascii_name(name_1)
summa_2 = ascii_name(name_2)
summa_3 = ascii_name(name_3)

print(compare_ascii_name(name_1, name_2, name_3))