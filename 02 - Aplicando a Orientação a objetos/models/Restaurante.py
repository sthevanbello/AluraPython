import random
class Restaurante:
    '''Classe de criação de restaurante 
    Inputs:
    - id = inteiro aleatório 
    - Nome
    - Categoria
    - ativo = False como padrão
    '''
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self.id = random.randint(1,1000)
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.lista_restaurantes.append(self)

    def __str__(self):
        return f'{str(self.id).ljust(5)}{self.nome.ljust(30)}{self.categoria.ljust(30)}{self.ativo}'

    def listar_restaurantes():
        for restaurante in Restaurante.lista_restaurantes:
            print(restaurante)
        print('='*100)