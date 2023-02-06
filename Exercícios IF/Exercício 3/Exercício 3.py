#Exercício 3
import math

r = float(input('Digite o valor do raio do círculo que se deseja calcular: '))
area = 2 * math.pi * r
perimetro = math.pi * math.pow(r, 2)

print('A área dada pelo raio concedido é de {}, e o prímetro de {}'.format(area, perimetro))