#Desafio 18
import math

angulo = float(input('Insira o valor do ângulo o qual se quer saber seno, cosseno e tangente: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('O valor do seno é: {:.2f}'.format(sen))
print('O valor do cosseno é: {:.2f}'.format(cos))
print('O valor da tangente é: {:.2f}'.format(tg))