import random
class Restaurante:
    def __init__(self, nome, categoria):
        self.id = random.randint(1,1000)
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    # nome = ''
    # categoria = ''
    # ativo = False

restaurante_krusty = Restaurante('Krusty Burger', 'Fast food')
restaurante_moe = Restaurante('Bar do Moe', 'Boteco')
restaurantes = [restaurante_krusty, restaurante_moe]

print(f'{'Id'.ljust(5)}{'Nome'.ljust(30)}{'Categoria'.ljust(30)}Estado\n')
print('-'*100)
for restaurante in restaurantes:
    print(dir(restaurante))
    print('-'*100)
    print(vars(restaurante))
    print('-'*100)
    print(f'{str(restaurante.id).ljust(5)}{restaurante.nome.ljust(30)}{restaurante.categoria.ljust(30)}{restaurante.ativo}')
    print('-'*100)