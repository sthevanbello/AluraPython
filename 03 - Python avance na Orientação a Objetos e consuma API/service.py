from models.Restaurante import Restaurante
from models.Cardapio.Bebida import Bebida
from models.Cardapio.Prato import Prato
from models.Cardapio.Sobremesa import Sobremesa
from models.Restaurante import Restaurante
import os

def separar_linha(caracter):
    print('')
    print(f'{caracter}'*100)
    print('')

restaurante_moe = Restaurante('bar do Moe', 'boteco')
bebida = Bebida('Cerveja duff', 5.00, 'Média')
prato = Prato('Macarronada', 25.00, 'Macarronada com salsicha')
sobremesa = Sobremesa('Sorvete', 8.00, 'Milho verde', 'Pote', 'Médio')
prato.aplicar_desconto()
bebida.aplicar_desconto()
restaurante_moe.adicionar_item_ao_cardapio(bebida)
restaurante_moe.adicionar_item_ao_cardapio(prato)
restaurante_moe.adicionar_item_ao_cardapio(sobremesa)

# os.system('cls' if os.name == 'nt' else 'clear')
# separar_linha('=')
# print(f'Nome'.ljust(30), 'Preço'.ljust(30), 'Descrição/Tamanho')
# separar_linha('-')
# print(bebida)
# print(prato)
# separar_linha('=')

os.system('cls' if os.name == 'nt' else 'clear')
# separar_linha('=')
# print(*restaurante_moe._cardapio, sep='\n')
restaurante_moe.listar_restaurante_cardapio();


def main():
    pass

if __name__ == '__main__':
    main()