import numpy as np

arr = [np.ones((3, 3))]
np.ones_like(arr)

print(arr)

import numpy as np


def matrices(f, c):
    valores = list(map(int, input('Introduce los valores: ').split()))
    matriz = np.array(valores).reshape(f, c)
    print(f'Matriz: \n {matriz}')


matrices(3, 3)
