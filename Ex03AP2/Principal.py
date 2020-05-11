import converter
r = float(input('Digite um valor em real: '))
print(f'O valor de {r:.2f} Reais equivale a: \n{converter.dolar(r):.2f} Dólares \n{converter.euro(r):.2f} Euros \n{converter.libra(r):.2f} Libras esterlinas.')

