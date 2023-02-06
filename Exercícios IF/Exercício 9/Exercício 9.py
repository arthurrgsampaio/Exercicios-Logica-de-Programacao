#Exercício 9
import math

altura = float(input('Digite a altura da lata de óleo em centímetros: '))
raio = float(input('Digite o raio da base da lata de óleo em centímetros: '))
vol = math.pi*math.pow(raio, 2)*altura

print('O volume da lata de óleo é {:.2f} cm³'.format(vol))