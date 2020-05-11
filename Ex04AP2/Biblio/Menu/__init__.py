def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('31mUsuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def lin(tam=42):
    return '-' * tam


def cabeça(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabeça('MENU DE OPÇÕES')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(lin())
    opc =  leiaInt('Escolha Uma Opção: ')
    return opc

