import random
class Restaurante:
    '''Classe de criação de restaurante 
    Inputs:
    - id = inteiro aleatório 
    - Nome
    - Categoria
    - ativo = False como padrão

    Methods:
    - listar_restaurantes()
    '''
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self.id = random.randint(1,1000)
        self._nome = nome.title()
        self._categoria = categoria.capitalize()
        self._ativo = False
        Restaurante.lista_restaurantes.append(self)

    def __str__(self):
        return f'{str(self.id).ljust(5)}{self._nome.ljust(30)}{self._categoria.ljust(30)}{self._ativo}'

    def listar_restaurantes():
        '''
        Método utilizado para listar todos os restaurantes inseridos
        '''
        print(f'{'Id'.ljust(5)}{'Nome'.ljust(30)}{'Categoria'.ljust(30)}Estado')
        print('-'*100)
        for restaurante in Restaurante.lista_restaurantes:
            print(restaurante)
        print('='*100)

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'


