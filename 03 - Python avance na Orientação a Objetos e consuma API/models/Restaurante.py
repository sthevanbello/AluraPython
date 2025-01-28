import random
from models.Avaliacao import Avaliacao
from models.Cardapio.item_cardapio import ItemCardapio
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
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.lista_restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(30)}{self._categoria.ljust(30)}{str(self.calcular_media_avaliacoes).ljust(30)}{self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        '''
        Método da classe utilizado para listar todos os restaurantes inseridos
        - Ao utilizar o @classmethod, utilizar o cls na assinatura do método
        '''
        print(f'{'Nome do Restaurante'.ljust(30)}{'Categoria'.ljust(30)}{'Avaliação'.ljust(30)}Estado')
        print('-'*100)
        for restaurante in cls.lista_restaurantes:
            print(restaurante)
        print('='*100)

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    def listar_avaliacoes(self):
        print(f'{'Cliente'.ljust(30)}{'Avaliação'}')
        print('-'*100)
        for avaliacao in self._avaliacoes:
            print(f'{avaliacao._cliente.ljust(30)}{avaliacao._nota}')

    @property
    def calcular_media_avaliacoes(self):
        if(len(self._avaliacoes) == 0):
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = soma / len(self._avaliacoes)
        return round(media, 1)

    def adicionar_item_ao_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def listar_restaurante_cardapio(self):
        self.listar_restaurantes()
        print('\nCardápio')
        print('-'*100)
        print('Item'.ljust(6),'Nome'.ljust(29), 'Preço'.ljust(29), 'Descrição/Tamanho')
        for item, item_cardapio in enumerate(self._cardapio, start=1):
            print(f'{str(item).ljust(7)}{item_cardapio}')