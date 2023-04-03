import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 15, 101)
y = np.sin(x)

print(x)
print(y)

plt.figure(figsize=(14, 7))                   # Задание размера полотна в дюймах

plt.plot(x,y , label='sin(x)', color='#4b0082', linewidth=4,
         marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
         markersize=10, markevery=5)

plt.plot(x, np.cos(x)/2, label='cos(x)/2', linewidth=3, color='lightcoral',
         marker='D', markeredgecolor='black', markevery=5)

plt.title('y = sin(x)')                       # Заголовок графика
plt.xlabel('Переменная X')                    # Надпись для оси x
plt.ylabel('Переменная Y')                    # Надпись для оси y

plt.legend()                                  # Отрисовка названий графиков ("легенды")

plt.grid()                                    # Отрисовка сетки

plt.show()                                    # Вывод графика

# marker – маркер;
# color – цвет линии;
# mec – цвет маркера;
# linestyle – стиль линии;
# label – подпись кривой графика;
# linewidth – ширина линии;
# markersize – размер маркера.