import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


x = pd.read_csv(f"{os.getcwd()}\\TraningSets\\itens.csv").values
y = pd.read_csv(f"{os.getcwd()}\\TraningSets\\price.csv").values

def define_function(x, y, w, b):
    m = len(x)
    f_wb = np.zeros(m)
    cost_sum = 0
    for i in range(m):
        f_wb[i] = (w*x[i]) + b
        cost = (f_wb[i] - y[i])**2
        cost_sum = cost_sum + cost
    total_cost = (1/(2*m))*cost_sum
    return f_wb, total_cost


w = 1.0
b = 0
y_cap, j_wb = define_function(x, y, w, b)
old_j_w = j_wb
old_j_wb = 0
while True:
    while True:
        y_cap, j_wb = define_function(x, y, w, b)
        if j_wb > old_j_w:
            old_j_w = j_wb
            break
        else:
            w += 0.1
            old_j_w = j_wb
    if old_j_w > old_j_wb:
        break
    else:
        b += 0.1
        old_j_wb = old_j_w

print(w,b,j_wb)

#plt.plot(range(0, 9), (y_cap - y)**2)
plt.plot(x, y_cap)
plt.scatter(x, y, marker="x", c="g")
plt.title('Gráfico de Pontos')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()