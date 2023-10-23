class Nome:
    def __init__(self, nome):
        self.nome = nome
        print(f'\033[1;4mNome: {self.nome}', end=' ')

class Sobrenome:
    def __init__(self, sobrenome):
        self.sobrenome = sobrenome
        print(self.sobrenome)

class Idade:
    def __init__(self, idade):
        self.idade = idade
        print(f'Idade: {self.idade}')

class Responsável:
    def __init__(self, responsável):
        self.responsável = responsável
        print(f'Responsável: {self.responsável}')

class Registro:
    def __init__(self, registro):
        self.registro = registro
        print(f'Registro - {self.registro}')
        print('\n')
