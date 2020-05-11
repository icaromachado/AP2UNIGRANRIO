from Ex04AP2.Biblio.Menu import *

def arqEX(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Não Conseguimos Criar o Arquivo')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabeça('LISTA DE PESSOAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<20} {dados[1]}')
    finally:
        a.close()

def cadastrar(arquivo, nome = 'Desconhecido', tel = 'Nenhum Contato'):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO!')
    else:
        try:
            a.write(f'{nome};{tel}\n')
        except:
            print('Erro ao preencher os dados!')
        else:
            print(f'CADASTRO DE {nome} FEITO COM SUCESSO!')