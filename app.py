import os
from functions import funcoes

restaurantes = [
{
    'nome': 'Praça',
    'categoria': 'Japonesa',
    'ativo': False
},
{
    'nome': 'Pizza Suprema',
    'categoria': 'Pizza',
    'ativo': True
},
{
    'nome': 'Cantina',
    'categoria': 'Italiano',
    'ativo': False
}]

def main():
    ''' Função principal que inicia o programa'''

    os.system('cls')
    funcoes.exibir_nome_do_programa()
    funcoes.exibir_opcoes()
    funcoes.escolher_opcao()

if __name__ == '__main__':
    main()