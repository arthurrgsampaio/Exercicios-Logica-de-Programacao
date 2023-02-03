#Desafio 17
import math

co = float(input('Insira o valor do comprimento do cateto oposto: '))
ca = float(input('Insira o valor do comprimento do cateto adjacente: '))
#h = math.sqrt(co**2 + ca**2) caso 1, sem a formula especifica para hipotenusa no math
h = math.hypot(ca, co)

print('O valor da hipotenusa com os valores inseridos é {}'.format(h))