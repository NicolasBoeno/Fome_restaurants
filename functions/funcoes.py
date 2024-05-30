import os
from app import main
from app import restaurantes

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela'''

    print("""

▒█▀▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▒█▀▀█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀█ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀ 
▒█▀▀▀ █░░█ █░▀░█ █▀▀ 　 ▒█▄▄▀ █▀▀ ▀▀█ ░░█░░ █▄▄█ █░░█ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ ▀▀█ 
▒█░░░ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀
     """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    ''' Exibe uma mensagem de opção inválida e retorna ao menu principal'''

    print('Opção inválida\n')
    voltar_ao_menu_principal()
    main()

def exibir_subtitulo(texto):
    ''' Exibe um subtitulo na tela'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo'''

    exibir_subtitulo('Finalizando aplicação...')
    exit()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal'''

    input('\nAperte uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    main()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''

    exibir_subtitulo('Listando os restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    #ljust alinha os texto em colunas com 20 espaços
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        #ljust alinha os texto em colunas com 20 espaços

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante
    
    Outputs: 
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            # not inverter false pra true e vice-versa
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()
