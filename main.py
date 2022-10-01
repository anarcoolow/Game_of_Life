from game import *
import numpy as np
import matplotlib

if __name__ == '__main__':
    mode = 1  # режим игры: 1 - Мур, 2 - Фон Нейман
    m = 25  # строк
    n = 25  # столбцов

    matplotlib.use('TkAgg')

    field = np.genfromtxt('field.csv', delimiter=',', dtype=int)

    play(field, m, n, mode)
