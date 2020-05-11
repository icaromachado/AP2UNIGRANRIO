class pessoa(object):

    def __init__(self, n, i, a, p, im):
        self.nome = n
        self.idade = i
        self.altura = a
        self.peso = p
        self.imc = im = a**2 / p

    def __repr__(self):
        return f'{self.nome} tem {self.idade} anos de idade.\nMede {self.altura}, Pesa {self.peso}kg.\nO IMC de {self.nome} é de {self.imc:.3f}'
