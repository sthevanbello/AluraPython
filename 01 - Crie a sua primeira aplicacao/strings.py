import os

lista_restaurantes = ['Krusty burger', 'Bar do Moe']

def exibir_titulo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')

def exibir_menu():

    print('*'*50)
    print(f'Menu')
    print('1 - Cadastrar restaurantes')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurantes')
    print('-'*50)
    print('4 - Sair\n')

def opcao_invalida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Opção inválida! Voltando ao menu inicial')
    voltar_menu_inicial()

def exibir_titulo_submenu(texto):
    exibir_titulo()
    print('*'*50)
    print(f'\n{texto}\n')
    print('-'*50)
    
def cadastrar_restaurante():
    while True:
        exibir_titulo_submenu('Cadastro de restaurante')
        restaurante = input('Digite o nome do restaurante: ')
        lista_restaurantes.append(restaurante)
        if len(lista_restaurantes) > 0:
            print(f'\nO restaurante: {restaurante} foi cadastrado com sucesso!\n')
        else:
            print('Tente novamente')
            cadastrar_restaurante()

        opcao = input('\nDeseja cadastrar mais um restaurante? S ou N: ')
        if opcao == 'N' or opcao == 'n':
            voltar_menu_inicial()
            break
        elif opcao == 'S' or opcao == 's':
            continue
        else:
            opcao_invalida()
            break

def voltar_menu_inicial():
    print('*'*50)
    input(f'\nAperte Enter para voltar ao menu inicial ')
    main()

def listar_restaurantes():
    exibir_titulo_submenu('Restaurantes cadastrados')
    if len(lista_restaurantes) > 0:
        # print(*lista_restaurantes, sep='\n')
        for item, restaurante in enumerate(lista_restaurantes):
            print(f'{item+1} - {restaurante}')
    else:
        print('Não há restaurantes cadastrados')
    voltar_menu_inicial()

def sair_do_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Saindo do programa')

def escolher_opcao():
    try:
        option_menu = int(input('Digite a opção: '))
        match(option_menu):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print(f'\nOpção escolhida: {option_menu}')
            case 4:
                sair_do_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()




def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
