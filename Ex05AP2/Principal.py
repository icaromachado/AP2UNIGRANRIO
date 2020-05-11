from classpessoa import pessoa

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = 0
p1 = pessoa(nome, idade, altura, peso, imc)
print(p1.__repr__())
