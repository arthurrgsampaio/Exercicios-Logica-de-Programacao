#Desafio 4
n = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(n)))
print('O que você digitou só possui espaços: {}'.format(n.isspace()))
print('O que você digitou é um número: {}'.format(n.isnumeric()))
print('O que você digitou é alfabético: {}'.format(n.isalpha()))
print('O que você digitou é alfanumérico: {}'.format(n.isalnum()))
print('O que você digitou está em maiúsculo: {}'.format(n.isupper()))
print('O que você digitou está em minúsculo: {}'.format(n.islower()))
print('O que você digitou está capitalizado: {}'.format(n.istitle()))
