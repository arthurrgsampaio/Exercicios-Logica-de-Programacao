#Exercício 6

n1 = float(input('Digite o valor do dividendo (valor qual será dividido): '))
n2 = float(input('Digite o valor do divisor (valor pelo qual o dividendo será dividido): '))
quociente = n1//n2
resto = n1%n2

print('O valor inteiro da divisão é {:.0f}, e o resto é {:.0f}'.format(quociente, resto))