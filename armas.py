

class Armas:
    def __init__(self, nome=None, classe=None, tipo=None, level_minimo=None, forca=None, destreza=None, resistencia=None):
        pass

    def __str__(self):
        return '{} ({} Lvl: {})'.format(self.nome, self.tipo, self.level_minimo)

    def mostrar_atributos(self):
        print('Força: {}\nDestreza: {}\nResistencia: {}\n'.format(self.forca, self.destreza,
                                                                             self.resistencia))


class Espadas(Armas):
    classe = 'Guerreiro'
    tipo = 'Espada'

    def __init__(self, nome, level_minimo, forca, destreza, resistencia):
        super()
        self.nome = nome
        self.level_minimo = level_minimo
        self.forca = forca
        self.destreza = destreza
        self.resistencia = resistencia


class Adagas(Armas):
    classe = 'Ladino'
    tipo = 'Adaga'

    def __init__(self, nome, level_minimo, forca, destreza, resistencia):
        super()
        self.nome = nome
        self.level_minimo = level_minimo
        self.forca = forca
        self.destreza = destreza
        self.resistencia = resistencia


class Arcos(Armas):
    classe = 'Arqueiro'
    tipo = 'Arcos'

    def __init__(self, nome, level_minimo, forca, destreza, resistencia):
        super()
        self.nome = nome
        self.level_minimo = level_minimo
        self.forca = forca
        self.destreza = destreza
        self.resistencia = resistencia


class Cajados(Armas):
    classe = 'Mago'
    tipo = 'Cajados'

    def __init__(self, nome, level_minimo, forca, destreza, resistencia):
        super()
        self.nome = nome
        self.level_minimo = level_minimo
        self.forca = forca
        self.destreza = destreza
        self.resistencia = resistencia


maca_de_guerra = Espadas('Maça de Guerra', 1, 3, 1, 6)
espada_curta = Espadas('Esoada Curta', 5, 15, 5, 30)
espada_bastarda = Espadas('Espada Bastarda', 15, 45, 15, 90)
espada_de_laminas_duplas = Espadas('Espadas de Laminas Duplas', 35, 105, 35, 210)
espada_grande = Espadas('Espada Grande', 50, 150, 50, 300)

adagas_simples = Adagas('Adagas simples', 1, 6, 2, 2)
adagas_com_mola = Adagas('Adagas com Mola', 5, 30, 10, 10)
adagas_de_aparar = Adagas('Adagas de Aparar', 15, 90, 30, 30)
adagas_de_ahlen = Adagas('Adagas de Ahlen', 35, 210, 70, 70)
adagas_venenosas = Adagas('Adagas Venenosas', 50, 300, 100, 100)

arco_composto = Arcos('Arco Composto', 1, 2, 6, 2)
arco_longo = Arcos('Arco Longo',5, 10, 30, 10)
arco_elfico = Arcos('Arco Élfico', 15, 30, 90, 30)
besta_leve = Arcos('Besta Leve', 35, 70, 210, 70)
besta_pesada = Arcos('Besta Pesada', 50, 100, 300, 100)

varinha_de_carmin = Cajados('Varinha de Carmin', 1, 1, 6, 3)
cajado_de_ametista = Cajados('Cajado de Ametista', 5, 5, 30, 15)
cetro_dagua = Cajados("Cetro d'agua", 15, 15, 90, 45)
Cajado_de_rubi = Cajados('Cajado de Rubi', 35, 35, 210, 105)
cajado_de_diamante = Cajados('Cajado de Diamante', 50, 50, 300, 150)

