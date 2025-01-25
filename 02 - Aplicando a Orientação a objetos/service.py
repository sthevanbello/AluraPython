from models.Restaurante import Restaurante
import os

restaurante_krusty = Restaurante('kruSty Burger', 'fast food')
restaurante_moe = Restaurante('bar do Moe', 'boteco')
restaurante_pizza_planet = Restaurante('pizza planet', 'Pizzaria')

restaurante_moe.alternar_estado()

# Restaurante.listar_restaurantes()

# print(restaurante_krusty)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()