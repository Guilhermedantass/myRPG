import personagens

NOME = input('Ola aventureiro, está preparado para uma nova aventura? Antes de tudo, nos diga seu nome: ')

print('Bom {}, para encarar essa aventura, qual classe mais se identifica com vc?'.format(NOME))
print(''' 1 - Guerreiro
 2 - Ladino
 3 - Arqueiro
 4 - Mago
''')

eu = personagens.Guerreiro(NOME)

print(eu)
print(eu.hp)
eu.mostrar_atributos()