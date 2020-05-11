lista = list()
pessoas = dict()
idad = media = 0
alt = altu_med = 0
while True:
    pessoas.clear()
    pessoas['codigo'] = int( input('Código: '))
    pessoas['nome'] = str( input('Nome: '))
    pessoas['idade']=int( input('Idade: '))
    idad += pessoas['idade']
    pessoas['altura'] = float( input('Altura: '))
    alt += pessoas['altura']
    lista.append(pessoas.copy())
    while True:
        resp = str(input('Deseja adicionar mais alguém ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*30)
print(f'Há {len(lista)} pessoas no total.')
media=idad / len(lista)
altu_med= alt / len(lista)

print(f'A média de idades é de {media:.2f} anos.')
print(f'A altura média das pessoas é de {altu_med:.2f} metros')
