# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

def terceiro_exercicio():
    numeros = range(1,11)
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            continue
        else:
            soma += numero
            print(f'{numero} ')
    print(f'A soma dos números ímpares de 1 a 10 é: {soma}')

def quarto_exercicio():

    numeros = list(range(1,11))
    numeros.sort(reverse = True)
    
    for numero in (numeros):
        print(numero)
    print(*numeros, sep=' - ')

def quinto_exercicio():
    numero = int(input('Digite um número inteiro positivo: '))
    for multiplicador in range(1,11):
        print(f'{numero} * {multiplicador} = {numero * multiplicador}')

def sexto_exercicio():
    numero = int(input('Digite um número inteiro positivo: '))
    lista = range(1,numero)
    soma = sum(lista)
    try:
        media = soma / len(lista)
        print(f'Media: {media}')
    except Exception as error:
        print('Lista vazia', error)

def main():
    # terceiro_exercicio()
    # quarto_exercicio()
    # quinto_exercicio()
    sexto_exercicio()

if __name__ == '__main__':
    main()
