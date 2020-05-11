from Ex04AP2.Biblio.Menu import *

from Ex04AP2.Biblio.Arquivo import *

arquivo = 'listadepessoas.txt'

if not arqEX(arquivo):
    criarArquivo(arquivo)

while True:
    resp = menu(['Adicionar Pessoa', 'Mostrar Lista de Pessoas'])
    if resp == 1:
        cabeça('NOVO CADASTRO')
        nome = input('Digite o Nome da Pessoa: ')
        tel = leiaInt('Digite o Telefone: ')
        cadastrar(arquivo, nome, tel)
    elif resp == 2:
        lerArquivo(arquivo)
    else:
        print('ERRO: Digite uma opção presente no Menu.')
