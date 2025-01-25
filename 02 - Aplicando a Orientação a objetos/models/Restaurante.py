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
        self._id = random.randint(1,1000)
        self._nome = nome.title()
        self._categoria = categoria.capitalize()
        self._ativo = False
        Restaurante.lista_restaurantes.append(self)

    def __str__(self):
        return f'{str(self._id).ljust(5)}{self._nome.ljust(30)}{self._categoria.ljust(30)}{self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        '''
        Método da classe utilizado para listar todos os restaurantes inseridos
        - Ao utilizar o @classmethod, utilizar o cls na assinatura do método
        '''
        print(f'{'Id'.ljust(5)}{'Nome'.ljust(30)}{'Categoria'.ljust(30)}Estado')
        print('-'*100)
        for restaurante in cls.lista_restaurantes:
            print(restaurante)
        print('='*100)

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo
