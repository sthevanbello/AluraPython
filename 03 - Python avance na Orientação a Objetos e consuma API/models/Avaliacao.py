class Avaliacao:
    '''Classe de Avaliação dos restaurantes

    Inputs:
    - Cliente
    - Nota
    '''
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = int(nota)