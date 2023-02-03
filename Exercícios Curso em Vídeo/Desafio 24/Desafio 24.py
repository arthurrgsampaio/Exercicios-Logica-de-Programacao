#Desafio 24
nc = str(input('Coloque o nome de uma cidade para saber se ela começa com santo: '))
certo = nc.strip().lower().count('santo', 0, 5)
if certo >0:
    print('Sim, começa')
else:
    print('Não, não começa')