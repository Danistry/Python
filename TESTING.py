matriz = []


def matrices(matriz):
    temp = []
    arr = []
    for i in range(3):
        temp.append(int(input('Introduzca numeros: ')))
    matriz.append(temp)

    for j in range(len(matriz)):
        if j % 2 == 0:
            arr.append(matriz[j])

    print(f' \n {arr}')


matrices(matriz)
