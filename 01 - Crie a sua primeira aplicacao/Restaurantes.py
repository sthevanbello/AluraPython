import os

# lista_restaurantes = ['Krusty burger', 'Bar do Moe']
lista_restaurantes = [
                        {'id': 1, 'nome': 'Krusty burger', 'categoria': 'Fast food', 'ativo': True},
                        {'id': 2, 'nome': 'Bar do Moe', 'categoria': 'Fast food', 'ativo': True},
                        {'id': 3, 'nome': 'Pizza Planet', 'categoria': 'Fast food', 'ativo': False}
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
    print(f'Menu Inicial')
    separar_linha('-')
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Alterar estado do restaurante')
    separar_linha('-')
    print('4 - Sair')

def opcao_invalida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Opção inválida!')

def exibir_titulo_submenu(texto):
    exibir_titulo()
    separar_linha('-')
    print(f'{texto}')
    separar_linha('-')
    
def cadastrar_restaurante():
    '''Função responsável por cadastrar um novo restaurante

    Inputs: 
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_titulo_submenu('Cadastro de restaurante')
    while True:
        nome_restaurante = input('Digite o nome do restaurante: ')
        categoria = input('Digite a categoria do restaurante: ')
        if nome_restaurante == '' or categoria == '':
            separar_linha('-')
            print('Não deixe campo em branco')
            input('Aperte Enter para continuar ')
            cadastrar_restaurante()
            break
        restaurante = {'id': len(lista_restaurantes)+1, 'nome':nome_restaurante, 'categoria': categoria, 'ativo': False}
        lista_restaurantes.append(restaurante)
        if restaurante in lista_restaurantes:
            separar_linha('-')
            print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
        else:
            print('Tente novamente')
            cadastrar_restaurante()
        separar_linha('-')
        opcao = input('Deseja cadastrar mais um restaurante? S ou N: ')
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
    separar_linha('-')
    input(f'Aperte Enter para voltar ao menu inicial ')
    main()

def listar_restaurantes(estado_solicitado = None):
    if len(lista_restaurantes) > 0:
        lista_restaurantes_atualizada = []
        for restaurante in lista_restaurantes:
            estado = 'Ativo' if restaurante['ativo'] else 'Inativo'
            if estado_solicitado == None:
                lista_restaurantes_atualizada.append(restaurante)
                # print(f'Id: {restaurante['id']} - Nome: {restaurante['nome']:30}Categoria: {restaurante['categoria']:30}Estado: {estado}')
            elif estado_solicitado == 'Ativo':
                if not restaurante['ativo']:
                    lista_restaurantes_atualizada.append(restaurante)
                    # print(f'Id: {restaurante['id']} - Nome: {restaurante['nome']:30}Categoria: {restaurante['categoria']:30}Estado: {estado}')
                else:
                    continue
            elif estado_solicitado == 'Inativo': 
                if restaurante['ativo']:
                    lista_restaurantes_atualizada.append(restaurante)
                    # print(f'Id: {restaurante['id']} - Nome: {restaurante['nome']:30}Categoria: {restaurante['categoria']:30}Estado: {estado}')
                else:
                    continue
        exibir_lista_restaurantes(lista_restaurantes_atualizada)
        return lista_restaurantes_atualizada
    else:
        print('Não há restaurantes cadastrados')

def exibir_lista_restaurantes(lista):
    if len(lista) > 0:
        print(f'{'Id'.ljust(5)}{'Nome'.ljust(30)}{'Categoria'.ljust(30)}Estado')
        separar_linha('.')
        for restaurante in lista:
            estado = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'{str(restaurante['id']).ljust(5)}{restaurante['nome'].ljust(30)}{restaurante['categoria'].ljust(30)}{estado}')
    else:
        print('Não há restaurantes')
    
def separar_linha(caracter):
    print('')
    print(f'{caracter}'*100)
    print('')

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
    lista_atual = listar_restaurantes(estado)
    try:
        opcao = 0
        if len(lista_atual) > 0:
            separar_linha('-')
            opcao = int(input('Digite o número do restaurante que terá seu estado alterado ou 0 (zero) para sair: '))
        else: 
            separar_linha('-')
            print(f'Só há restaurantes com estado {estado}')
        if opcao == 0:
            voltar_menu_inicial()
        elif opcao > 0:
            restaurante = None
            for item in lista_atual:
                if item['id'] == opcao:
                    restaurante = item
                    break
            estado_atual = True if estado == 'Ativo' else False
            if estado_atual in restaurante.values():
                separar_linha('-')
                print(f'Restaurante já está com o estado {estado}!\n')
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
        alterar_estado_restaurante(estado)
        
def sair_do_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Saindo do programa')

def escolher_opcao():
    try:
        separar_linha('-')
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
