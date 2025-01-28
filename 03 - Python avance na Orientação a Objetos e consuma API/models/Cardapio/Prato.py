from models.Cardapio.itens_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome.ljust(30)}R${str(self._preco).ljust(28)}{self._descricao.ljust(30)}'