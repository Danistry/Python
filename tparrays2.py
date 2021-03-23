# act1
# Señor programador el codigo debe aceptar numeros flotantes, e imprimirlos en el orden que entra y a su vez
# eliminarlos 1 a uno, puede modificar el existente o hacer el propio, good luck!

def cajero():
    caja = []

    for i in range(1, 11):
        caja.append(float(input('Ingrese los valores de la caja: ')))

    print(f'\nNumbers entered: {caja} \n')

    print('removing elements...')

    caja.pop(0)
    print(caja)

    print('\nDeleted items')


cajero()

#act2
vector = [5, 7, 9, 2, 4]


def analisis(vector, n):
    if n < vector[0]:
        vector.insert(0, n)
    elif n > vector[0]:
        vector.insert(1, n)

    print(vector)


analisis(vector, 3)

#act3
names = ['Daniel Alejandro Ojeda', 'Cristian Ojeda', 'Heejin']


def registro(names, voto):

    if voto in names:
        print(f'Esta persona si puede votar: {voto}')
    elif voto not in names:
        print(f'Esta persona no esta en la lista: {voto}')


registro(names, 'Cristian Ojeda')

#act4

vector = ['Fashion', 'Ropa comoda', 'Start']


def Fashion(vector):
    name = ''
    temporal = ''

    for i in range(len(vector)):
        if ' ' in vector[i]:
            vector = vector.split()

            for j in range(len(vector[i])):
                temporal += f'-{vector[i][j]}'

            name += temporal
        else:
            name = f'-{vector[i]}'

    name = name.replace('-', ' ')
    return print(name)


Fashion(vector)

#act5

vec = ['extraño', 'mucho']


def solito(vec, word):

    for i in range(len(vec)):
        if word in vec[i]:
            vec.remove(word)
            break
        else:
            vec.insert(0, word)
            break

    return print(vec)


solito(vec, 'Te')

#act 6

vector = [True, 0, 'Hola pete']


def texto(vector):

    for i in range(len(vector)):
        if type(vector[i]) == str:
            return print(f'El dato de tipo str esta en la posicion: {i}')




texto(vector)

#act 7
vector = 'Hola te extraño lpm'


def array(vector):
    return print(vector.split(' '))


array(vector)

#act 8

vector = 'Hola te extraño lpm'


def array(vector):
    vec = []
    vector = vector.split(' ')

    for i in range(len(vector)):
        if i % 2 == 0:
            vec.append(vector[i])

    return print(vec)


array(vector)

#act9
l1 = ['French', 'English', 'German']
l2 = ['Spanish', 'Portuguese']
boo = False


def concat(l1, l2, boo):
    if boo is True:
        l1 += l2
        return print(l1)
    elif boo is False:
        l2 += l1
        return print(l2)


concat(l1, l2, boo)


#act10

vector = ['h', 'd,''s', 'j', 'f', 'g', 'k', 's', 'l', 'd', 'f', '#', 'e', 'r', 7, 5, 6, 's', 5, 'ñ']


def numerico(vector):
    arr = []

    for i in range(len(vector)):
        if type(vector[i]) is int:
            arr.append(vector[i])

    return print(arr)


numerico(vector)

#act11

pos = ["unidad", "decena", "centena", "millar"]


def quiniela(pos):
    num = []
    for i in range(len(pos)):
        num.append(int(input(f'Ingrese un numero: ')))
        print(f'{num[i]} en la {pos[i]}')

    return print(num)


quiniela(pos)

#act12
vec = "Persiana americana. Corazón delator. Crimen"


def revers(vec):
    arr = vec.split('.').reverse()
    arr.reverse()
    print(arr)

revers(vec)





