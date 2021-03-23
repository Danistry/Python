#act2
arra = [1.5, 2.2, 4.5, 3.1, 2.5, 3.3, 1.6, 2.2, 4.1, 1.3, 3.1]


def peso(arra):
    prom_Peso = int(0)

    for i in arra:
        prom_Peso += i

    prom_Peso = prom_Peso / len(arra)
    return print(format(prom_Peso, ".2f"))


peso(arra)

#act4
name = ['Eliseo Rodriguez', 'Alma Alves', 'Cynthia Cerdan']


def orden(name):
    return print(sorted(name))


orden(name)

#act5
valore = [1.5, 2.5, 50.60, 10.6, 9.6]


def descent(valore):
    return print(sorted(valore, reverse=True))


descent(valore)

#act8

names = ["Carlos María", "Jessica Yolanda", "Mario Raul", "Dahiana Pamela"]
deudas = [3.600, 21.543, 0, 8.145]


def clinica(names, deudas):
    deudores = []

    for i in range(len(deudas)):
        if deudas[i] != 0:
            deudores.append(names[i])

    print(f'Personas con deudas: {deudores}')


print()
clinica(names, deudas)


def al_Dia(names, deudas):
    corriente = []

    for i in range(len(deudas)):
        if deudas[i] == 0:
            corriente.append(names[i])

    print(f'Personas al dia: {corriente}')


print()
al_Dia(names, deudas)


def informe(names, deudas):
    prom = int(0)
    res = []

    for i in range(len(deudas)):
        prom += i

    prom = prom / len(deudas)

    for i in range(len(deudas)):
        if deudas[i] > prom:
            res.append(names[i])

    print(f'Personas al corriente de pago: {res}')


print()
informe(names, deudas)


