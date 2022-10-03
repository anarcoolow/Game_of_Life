import numpy as np

def generate(m: int, n: int):
    field = np.zeros((m, n))

    np.savetxt("field.csv", field, fmt="%d", delimiter=",")
