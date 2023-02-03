#Desafio 27
nomec = str(input('Insira seu nome completo: ')).strip()
dividido = nomec.split()
print('Seu primeiro e último nomes são: {} e {}, consecutivamente'.format(dividido[0], dividido[-1]))