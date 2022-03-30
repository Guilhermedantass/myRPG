import personagens
import armas

NOME = input('Ola aventureiro, está preparado para uma nova aventura? Antes de tudo, nos diga seu nome: ')

# print('Bom {}, para encarar essa aventura, qual classe mais se identifica com vc?'.format(NOME))
# print(''' 1 - Guerreiro
#  2 - Ladino
#  3 - Arqueiro
#  4 - Mago
# ''')

eu = personagens.Guerreiro(NOME, level=2, forca=10, destreza=0, resistencia=5)
print(eu)
eu.mostrar_atributos()

eu.conquistar_equipamento(armas.maca_de_guerra)
eu.conquistar_equipamento(armas.espada_grande)
eu.equipar_armas()
eu.mostrar_atributos()