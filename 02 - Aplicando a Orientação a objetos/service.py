from models.Restaurante import Restaurante
import os

# restaurante_krusty = Restaurante('kruSty Burger', 'fast food')
restaurante_moe = Restaurante('bar do Moe', 'boteco')
# restaurante_pizza_planet = Restaurante('pizza planet', 'Pizzaria')

restaurante_moe.alternar_estado()
restaurante_moe.receber_avaliacao('Homer', 8)
restaurante_moe.receber_avaliacao('Marge', 5)
restaurante_moe.receber_avaliacao('Lisa', 4.5)
restaurante_moe.receber_avaliacao('Bart', 7)
restaurante_moe.receber_avaliacao('Leny', 9)
restaurante_moe.receber_avaliacao('Barney', 10)
restaurante_moe.listar_avaliacoes()
# Restaurante.listar_restaurantes()

# print(restaurante_krusty)

def main():
    # os.system('cls' if os.name == 'nt' else 'clear')
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()