from models.Cardapio.itens_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome.ljust(30)}{str(self._preco).ljust(30)}{self._tamanho.ljust(30)}'