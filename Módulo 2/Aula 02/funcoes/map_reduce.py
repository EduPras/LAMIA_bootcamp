from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

def mais_um_meio(nota):
    return nota+1.5

notas = [6.4, 7.2, 5.8, 8.4]
# notas_finais = list(map(mais_um_meio, notas))
notas_finais_1 = list(map(somar_nota(1.5), notas))
notas_finais_2 = list(map(somar_nota(1.6), notas))
print(notas_finais_1, notas_finais_2)

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)
# procedural
# for i, nota in enumerate(notas):
    # notas[i] += nota + 1.5
    