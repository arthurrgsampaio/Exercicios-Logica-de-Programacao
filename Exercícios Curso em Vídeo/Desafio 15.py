#Desafio 15
dias = int(input('Insira quantos dias o carro foi alugado: '))
km = float(input('Insira quantos quilômetros foram rodados com o carro: '))
valor = (dias*60)+(0.15*km)
print('Ao alugar o carro por {:.0f} dias, e rodar {:.2f}km, o valor do aluguel foi de R${:.2f}'.format(dias, km, valor))