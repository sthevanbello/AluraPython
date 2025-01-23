import os

def exibir_titulo():
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
    print(f'Opção inválida')
    input(f'Aperte Enter para voltar ao menu inicial')
    main()

def sair_do_app():
    print('Saindo do programa')

def escolher_opcao():
    try:
        option_menu = int(input('Digite a opção: '))
        match(option_menu):
            case 1:
                print (f'\nOpção escolhida: {option_menu}')
            case 4:
                sair_do_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()




def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_titulo()
    exibir_menu()
    escolher_opcao()
    

if __name__ == '__main__':
    main()
