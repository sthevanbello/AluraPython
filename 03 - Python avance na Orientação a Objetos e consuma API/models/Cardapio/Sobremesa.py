from models.Cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tipo = tipo
        self._tamanho = tamanho

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)

    def __str__(self):
        return f'{self._nome.ljust(30)}R${f"{self._preco:.2f}".ljust(28)}{self._descricao.ljust(30)}{self._tipo.ljust(30)}{self._tamanho.ljust(30)}'