import personagens
import armas

NOME = input('Ola aventureiro, está preparado para uma nova aventura? Antes de tudo, nos diga seu nome: ')

print('Bom {}, para encarar essa aventura, qual classe mais se identifica com vc?'.format(NOME))
print(''' 1 - Guerreiro
 2 - Ladino
 3 - Arqueiro
 4 - Mago
''')

eu = personagens.Guerreiro(NOME, forca=10, destreza=0,resistencia=5)

print(eu)
eu.mostrar_atributos()