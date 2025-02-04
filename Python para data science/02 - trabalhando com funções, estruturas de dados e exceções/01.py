from random import choice, choices, randrange
from math import pow, sqrt, pi

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

# inteiros = [(sqrt(numero), numero) for numero in numeros if sqrt(numero) // 1 == sqrt(numero)]
# print(*inteiros, sep='\n')
# raio = 20
# area_circulo = pi * pow(raio, 2)
# print(f'{raio}')
# print(f'Área: {area_circulo:.2f}')
# valor = 25 * area_circulo
# print(f'Valor a ser pago: {valor:.2f}')

def calcular_media(lista: list=[0]) -> float:
    return sum(lista) / len(lista)

# media = calcular_media(numeros)
# print(media)
# qualitativo = 0.5
# numero_atualizado = lambda x: x + qualitativo

# print(numero_atualizado(6))

# numeros_atualizados = map(lambda x: x + qualitativo, numeros)
# print(list(numeros_atualizados))

# alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
# pesos = [65, 80, 58, 70, 95]

# imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
# print(imc)

nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]

estudantes = {nomes_estudantes[i]: medias_estudantes[i] for i in range(len(nomes_estudantes)) if medias_estudantes[i] >= 9.0}
print(estudantes)
bolsistas = {nome: media 
            for nome, media in zip(nomes_estudantes, medias_estudantes) 
            if media >= 9.0}
print(bolsistas)