import os

# lista_restaurantes = ['Krusty burger', 'Bar do Moe']
lista_restaurantes = [{'Krusty burger': True}, {'Bar do Moe': True}, {'Pizza Planet': False}]

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
    print(f'Opção inválida!')

def exibir_titulo_submenu(texto):
    exibir_titulo()
    print('*'*50)
    print(f'\n{texto}\n')
    print('-'*50)
    
def cadastrar_restaurante():
    while True:
        nome_restaurante = input('Digite o nome do restaurante: ')
        restaurante = {nome_restaurante: False}
        lista_restaurantes.append(restaurante)
        if restaurante in lista_restaurantes:
            print(f'\nO restaurante: {nome_restaurante} foi cadastrado com sucesso!\n')
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
            voltar_menu_inicial()
            break

def voltar_menu_inicial():
    input(f'\nAperte Enter para voltar ao menu inicial ')
    main()

def listar_restaurantes():
    if len(lista_restaurantes) > 0:
        # print(*lista_restaurantes, sep='\n')
        for item, restaurante in enumerate(lista_restaurantes):
            for nome, ativo in restaurante.items():
                descricao = 'Inativo'
                if ativo:
                    descricao = 'Ativo'
                print(f'{item+1} - {nome}: {descricao}')
        print('-'*50)
        print()
    else:
        print('Não há restaurantes cadastrados')

def ativar_restaurante():
    exibir_titulo_submenu('Ativar restaurante')
    listar_restaurantes()
    try:
        opcao = int(input('Digite o número do restaurante que será ativado ou 0 (zero) para sair: '))
        if opcao == 0:
            voltar_menu_inicial()
        elif opcao > 0 and len(lista_restaurantes) >= opcao:
            restaurante = lista_restaurantes[opcao-1]
            if True in restaurante.values():
                print('-'*50)
                print(f'\nRestaurante já está ativo!\n')
                print('-'*50)
                input('Aperte Enter para continuar ')
            else:
                for nome, ativo in restaurante.items():
                    restaurante[nome] = True
                    if True in restaurante.values():
                        print('-'*50)
                        print(f'Restaurante {nome} ativado com sucesso!')
                        print('-'*50)
                        input('Aperte Enter para continuar ')
                    else:
                        print('-'*50)
                        input('Aperte Enter para tentar novamente ')
            ativar_restaurante()
        else:
            opcao_invalida()
            print('-'*50)
            input('Aperte Enter para tentar novamente ')
            ativar_restaurante()
    except Exception as e:
        opcao_invalida()
        print('-'*50)
        input('Aperte Enter para tentar novamente ')
        ativar_restaurante()
        
def sair_do_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Saindo do programa')

def escolher_opcao():
    try:
        option_menu = int(input('Digite a opção: '))
        match(option_menu):
            case 1:
                exibir_titulo_submenu('Cadastro de restaurante')
                cadastrar_restaurante()
            case 2:
                exibir_titulo_submenu('Restaurantes cadastrados')
                listar_restaurantes()
                voltar_menu_inicial()
            case 3:
                ativar_restaurante()
            case 4:
                sair_do_app()
            case _:
                opcao_invalida()
                voltar_menu_inicial()
    except Exception as e:
        opcao_invalida(e)
        voltar_menu_inicial()




def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
