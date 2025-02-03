from random import choice, choices, randrange
from math import pow, sqrt

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

# print(choice(lista))

# print(randrange(1,100))

# print(pow(2,3))

# lista_participantes = range(1,1000)
# print(*lista_participantes, sep='-')
# print(choice(lista_participantes))

# token = randrange(1000,9998,2)
# print(token)

# frutas = ["maçã", "banana", "uva", "pêra", 
#         "manga", "coco", "melancia", "mamão",
#         "laranja", "abacaxi", "kiwi", "ameixa"]

# frutas_selecionadas = choices(frutas,k=3)
# print(frutas_selecionadas)

numeros = [2, 8, 15, 23, 91, 112, 121, 256, 225]
# inteiros = []
# for numero in numeros:
#     raiz = sqrt(numero)
#     if raiz // 1 == raiz:
#         inteiros.append((numero, int(raiz)))
# print(*inteiros, sep='\n')

inteiros = [(sqrt(numero), numero) for numero in numeros if sqrt(numero) // 1 == sqrt(numero)]
print(*inteiros, sep='\n')