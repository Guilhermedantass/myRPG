import random

NOMES = ['Lucas', 'Guilherme', 'João', 'Aquiles', 'Pablo', 'Lorenzo',
         'Murilo', 'Caio', 'Renan', 'Marcelo', 'Gabriel', 'João', 'Vicente',
         'Bryan', 'Leonardo', 'Letícia', 'Gabriela', 'Carolina', 'Isa', 'Dulce'
         ]


class Personagens:

    def __init__(self, nome=None, nivel=None, classe=None, equipamento=None, bec=None, forca=None, constitucao=None,
                 inteligencia=None, percepcao=None):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        if nivel:
            self.nivel = nivel
        else:
            self.nivel = random.randint(1, 100)

    def __str__(self):
        return '{} ({} - Lvl: {})'.format(self.nome, self.classe, self.nivel)


class Guerreiro(Personagens):
    classe = 'Guerreiro'


class Ladino(Personagens):
    classe = 'Ladino'


class Arqueiro(Personagens):
    classe = 'Arqueiro'


class Mago(Personagens):
    classe = 'Mago'


eu = Guerreiro('guilherme')
print(eu)
