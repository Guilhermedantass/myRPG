import random

import armas

NOMES = ['Lucas', 'Guilherme', 'João', 'Aquiles', 'Pablo', 'Lorenzo',
         'Murilo', 'Caio', 'Renan', 'Marcelo', 'Gabriel', 'João', 'Vicente',
         'Bryan', 'Leonardo', 'Letícia', 'Gabriela', 'Carolina', 'Isa', 'Dulce'
         ]


class Personagem:

    def __init__(self, nome=None, level=None, classe=None, hp=22, forca=None,
                 resistencia=None, destreza=None, forca_total=None, resistencia_total=None, destreza_total=None,
                 pontos_de_atributos=15, arma=None, equipamentos=[], atk=None, defesa=None,
                 xp_atual=0, xp_upar=20):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        self.equipamentos = equipamentos
        self.arma = arma

        self.hp = int(hp + 3*self.level)

        if forca or resistencia or destreza:
            self.forca = forca
            self.resistencia = resistencia
            self.destreza = destreza

        else:
            self.forca = random.randint(0, pontos_de_atributos)
            self.resistencia = random.randint(0, pontos_de_atributos)
            self.destreza = pontos_de_atributos

        self.forca_total = self.forca
        self.destreza_total = self.destreza
        self.resistencia_total = self.resistencia

        self.atk = self.forca_total + self.destreza_total
        self.defesa = self.resistencia_total

        self.xp_atual = xp_atual
        self.xp_upar = xp_upar

    def __str__(self):
        return '{} ({} - Lvl: {})'.format(self.nome, self.classe, self.level)

    def mostrar_atributos(self):
        print('Força: {}\n Destreza: {}\n Resistencia: {}\n HP: {}\n'.format(self.forca_total, self.destreza_total,
                                                                    self.resistencia_total, self.hp))

    def conquistar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def mostrar_equipamentos(self):
        for i, equipamento in enumerate(self.equipamentos):
            print('{} - {}'.format(i, equipamento))
            equipamento.mostrar_atributos()

    def equipar_armas(self):
        self.mostrar_equipamentos()

        while True:
            arma_escolhida = input('Escolha sua arma: ')

            try:
                arma_escolhida = int(arma_escolhida)
                if self.level >= self.equipamentos[arma_escolhida].level_minimo:
                    self.arma = self.equipamentos[arma_escolhida]
                    break
                else:
                    print('Você ainda não esta praparado para essa arma')

            except:
                print('Escolha inválida')

        if self.classe == self.arma.classe:
            self.forca_total = self.forca + self.arma.forca * 1.30
            self.destreza_total = self.destreza + self.arma.destreza * 1.30
            self.resistencia_total = self.resistencia + self.arma.resistencia * 1.30
            print('Buff ativo')
        else:
            self.forca_total = self.forca + self.arma.forca
            self.destreza_total = self.destreza_total + self.arma.destreza
            self.resistencia_total = self.resistencia + self.arma.resistencia

    def upar(self):
        if self.level < 50:
            self.level += 1

    def ganhar_xp(self, xp):
        self.xp_atual += xp

        if self.xp_atual >= self.xp_upar:
            self.upar()
            self.xp_upar += (self.level * 2 * 5)



class Guerreiro(Personagem):
    classe = 'Guerreiro'


class Ladino(Personagem):
    classe = 'Ladino'


class Arqueiro(Personagem):
    classe = 'Arqueiro'


class Mago(Personagem):
    classe = 'Mago'
