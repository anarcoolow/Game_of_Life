import numpy as np
import matplotlib.pyplot as plt


def show(field: np.ndarray, pause_time):
    plt.imshow(field)
    plt.draw()
    plt.pause(pause_time)
    plt.clf()


def play(field: np.ndarray, m: int, n: int, mode: int):
    EPOCHS = 100
    PAUSE_TIME = 0.01

    plt.ion()
    show(field, PAUSE_TIME)
    exit_counter = 0
    for _ in range(EPOCHS):
        field = epoch(field, m, n, mode)
        show(field, PAUSE_TIME)
        if field.sum() == 0:
            exit_counter += 1
        if exit_counter > PAUSE_TIME / (PAUSE_TIME ** 2):
            exit()


def get_values_of_neighbors(field: np.ndarray, i: int, j: int, m: int, n: int, mode: int) -> np.ndarray:
    values = []
    if mode == 1:
        for k in range(i - 1, i + 2):
            for p in range(j - 1, j + 2):
                if (k >= 0 and p >= 0) and (k < m and p < n) and not (k == i and p == j):
                    values.append(field[k][p])
    elif mode == 2:
        terms = [-1, 1]
        for term in terms:
            k = i + term
            if 0 <= k < m:
                values.append(field[k][j])
            k = j + term
            if 0 <= k < n:
                values.append(field[i][k])

    return np.array(values, dtype=int)


def epoch(old_field: np.ndarray, m: int, n: int, mode: int) -> np.ndarray:
    new_field = np.zeros((m, n), dtype=int)

    for i in range(m):
        for j in range(n):
            neighbors = get_values_of_neighbors(old_field, i, j, m, n, mode)
            if old_field[i][j] == 1 and (1 < neighbors.sum() < 4):
                new_field[i][j] = 1
            elif old_field[i][j] == 0 and neighbors.sum() == 3:
                new_field[i][j] = 1
            else:
                new_field[i][j] = 0

    return new_field
