#Desafio 13
si = float(input('Digite o valor do salário antes do aumento: '))
aumento = float(input('Insira qual a porcentagem de aumento do salário: '))
a = aumento/100
sf = si+(si*a)
print('O salário após o aumento de {}%, ficou em R${}'.format(aumento, sf))