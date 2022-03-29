import random


NOMES = ['Lucas', 'Guilherme', 'João', 'Aquiles', 'Pablo', 'Lorenzo',
         'Murilo', 'Caio', 'Renan', 'Marcelo', 'Gabriel', 'João', 'Vicente',
         'Bryan', 'Leonardo', 'Letícia', 'Gabriela', 'Carolina', 'Isa', 'Dulce'
         ]


class Personagem:

    def __init__(self, nome=None, level=None, classe=None, forca=None, hp=22,
                 resistencia=None, destreza=None, pontos_de_atributos=15, arma=None,
                 armadura=None, calca=None, atk=None, defesa=None):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        self.hp = int(hp + 3*self.level)

        if forca or resistencia or destreza:
            self.forca = forca
            self.resistencia = resistencia
            self.destreza = destreza
        else:
            self.forca = random.randint(0, pontos_de_atributos)
            self.resistencia = random.randint(0, pontos_de_atributos)
            self.destreza = pontos_de_atributos

        self.atk = self.forca + self.destreza
        self.defesa = self.destreza

    def __str__(self):
        return '{} ({} - Lvl: {})'.format(self.nome, self.classe, self.level)

    def mostrar_atributos(self):
        print('Força: {}\n Destreza: {}\n Resistencia: {}\n HP: {}\n'.format(self.forca, self.destreza, self.resistencia, self.hp))


class Guerreiro(Personagem):
    classe = 'Guerreiro'


class Ladino(Personagem):
    classe = 'Ladino'


class Arqueiro(Personagem):
    classe = 'Arqueiro'


class Mago(Personagem):
    classe = 'Mago'
