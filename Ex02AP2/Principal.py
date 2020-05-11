lista = list()
produtos = dict()
valor = media = 0
while True:
    produtos.clear()
    produtos['codigo'] = int(input('Código do Produto: '))
    produtos['nome'] = str(input('Nome do Produto: '))
    produtos['preço'] = float(input('Preço do produto: '))
    valor += produtos['preço']
    lista.append(produtos.copy())
    while True:
        resp = str(input('Deseja cadastrar mais produtos ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
         break
media = valor / len(lista)
print(f'O valor médio dos produtos cadastrados é de {media:.2f} reais.')
print(f'Os produtos com o preço acima da média são: ', end='')
for p in lista:
    if p['preço'] > media:
        print(f'{p["nome"]} ', end='')
print('.')
