#Exercício 1

base = float(input('Digite o valor da base do retângulo: '))
altura = float(input('Agora, digite o valor da altura do retângulo: '))
area = base * altura
perimetro = (2*base) + (2*altura)

print('O valor da área do retângulo é de {}, e seu perímetro é de {}'.format(area, perimetro))