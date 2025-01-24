import os

# lista_restaurantes = ['Krusty burger', 'Bar do Moe']
lista_restaurantes = [
                        {'nome':'Krusty burger', 'categoria': 'Fast food', 'ativo': True},
                        {'nome':'Bar do Moe', 'categoria': 'Fast food', 'ativo': True},
                        {'nome': 'Pizza Planet', 'categoria': 'Fast food', 'ativo': False}
                    ]

lista_estados = ['Ativo', 'Inativo']
    
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

    separar_linha('-')
    print(f'Menu')
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Alterar estado do restaurante')
    separar_linha('-')
    print('4 - Sair\n')

def opcao_invalida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Opção inválida!')

def exibir_titulo_submenu(texto):
    exibir_titulo()
    separar_linha('-')
    print(f'\n{texto}\n')
    separar_linha('-')
    
def cadastrar_restaurante():
    exibir_titulo()
    exibir_titulo_submenu('Cadastro de restaurante')
    while True:
        nome_restaurante = input('Digite o nome do restaurante: ')
        categoria = input('Digite a categoria do restaurante: ')
        restaurante = {'nome':nome_restaurante, 'categoria': categoria, 'ativo': False}
        lista_restaurantes.append(restaurante)
        if restaurante in lista_restaurantes:
            print(f'\nO restaurante: {nome_restaurante} foi cadastrado com sucesso!\n')
        else:
            print('Tente novamente')
            cadastrar_restaurante()
        separar_linha('-')
        opcao = input('\nDeseja cadastrar mais um restaurante? S ou N: ')
        if opcao == 'N' or opcao == 'n':
            voltar_menu_inicial()
            break
        elif opcao == 'S' or opcao == 's':
            cadastrar_restaurante()
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
            estado = 'Inativo'
            if restaurante['ativo']:
                estado = 'Ativo'
            print(f'{item+1} - Nome: {restaurante['nome']:30}Categoria: {restaurante['categoria']:30}Estado: {estado}')
        separar_linha('-')
    else:
        print('Não há restaurantes cadastrados')

def separar_linha(caracter):
    print(f'{caracter}'*100)
    print()

def alterar_restaurante():
    exibir_titulo_submenu('Alterar o estado do restaurante')
    try:
        for item, estado in enumerate(lista_estados):
            print(f'{item+1} - {estado}')
        separar_linha('-')
        opcao = int(input('Deseja alterar o estado para qual modo? '))
        alterar_estado_restaurante(lista_estados[opcao-1])
    except:
        opcao_invalida()
        alterar_restaurante()

def alterar_estado_restaurante(estado):
    exibir_titulo_submenu(f'Alterar estado do restaurante para {estado}')
    listar_restaurantes()
    try:
        opcao = int(input('Digite o número do restaurante que terá seu estado alterado ou 0 (zero) para sair: '))
        if opcao == 0:
            voltar_menu_inicial()
        elif opcao > 0 and len(lista_restaurantes) >= opcao:
            restaurante = lista_restaurantes[opcao-1]
            estado_atual = False
            if estado == 'Ativo':
                estado_atual = True
                
            if estado_atual in restaurante.values():
                separar_linha('-')
                print(f'\nRestaurante já está com o estado {estado}!\n')
                separar_linha('-')
                input('Aperte Enter para continuar ')
            else:
                restaurante['ativo'] = estado_atual
                if estado_atual in restaurante.values():
                    separar_linha('-')
                    print(f'Restaurante {restaurante['nome']} alterado com sucesso!')
                    separar_linha('-')
                    input('Aperte Enter para continuar ')
                else:
                    separar_linha('-')
                    input('Aperte Enter para tentar novamente ')
            alterar_estado_restaurante(estado)
        else:
            opcao_invalida()
            separar_linha('-')
            input('Aperte Enter para tentar novamente ')
            alterar_estado_restaurante(estado)
    except Exception as e:
        opcao_invalida()
        separar_linha('-')
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
                cadastrar_restaurante()
            case 2:
                exibir_titulo_submenu('Restaurantes cadastrados')
                listar_restaurantes()
                voltar_menu_inicial()
            case 3:
                alterar_restaurante()
            case 4:
                sair_do_app()
            case _:
                opcao_invalida()
                voltar_menu_inicial()
    except Exception as e:
        opcao_invalida()
        voltar_menu_inicial()




def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
