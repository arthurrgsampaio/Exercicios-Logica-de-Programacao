#Desafio 22
nome = str(input('Insira o seu nome completo: ')).strip()

print('Nome todo maiúsculo: {}'.format(nome.upper()))
print('Nome todo minúsculo: {}'.format(nome.lower()))
print('Qunantas letras tem seu nome completo: {}'.format(len(nome)-nome.count(' ')))
print('Quantas letras tem seu primeiro nome: {}'.format(len(nome.split()[0])))