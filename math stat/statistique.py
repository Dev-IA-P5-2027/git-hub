from itertools import accumulate
from statistics import mode

nombre_de_piece = [1, 2, 3, 4, 5, 6, 7]
nombre_appartement = [48, 72, 96, 64, 39, 25, 3]
liste = []

# def BDD(nombre_de_piece : int, nombre_appartement : int):
#     for x, y in zip(nombre_de_piece, nombre_appartement):
#         stat = (list(nombre_de_piece[x]*nombre_appartement[y]))
#     return stat

#=== Version galérien ===

def printer():
    for x, y in zip(nombre_de_piece, nombre_appartement):
        # for value in nombre_de_piece:
        résultat = liste.append(list(str(x))*y)
    return résultat

# affiche = printer()
# print(liste)

#=== Version propre avec extend
def printer2():
    for x, y in zip(nombre_de_piece, nombre_appartement):
        liste.extend([x] * y)
    return liste

result = printer2()
print(result)
# print(liste)

#=== Effectif cumulé

effectif_cumules = list(accumulate(nombre_appartement))
print(effectif_cumules[-1])


N = 1 / 347

#=== Moyenne ===

def moyenne(liste):
    return sum(liste) / len(liste) if liste else 0

Moyenne = (moyenne(result))
print(Moyenne)

#=== Variance ===
def Varianced():
    for value in result:
        Variance = N*((347*(value - Moyenne))**2)
    return Variance

Variance_1 = print(Varianced())


Mediane = (347+1) / 2
print(Mediane)
print(f"la médiane est {result[174]}")




