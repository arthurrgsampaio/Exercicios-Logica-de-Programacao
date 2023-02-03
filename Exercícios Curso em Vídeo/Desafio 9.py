#Desafio 9
t = int(input('Digite o número inteiro o qual se deseja saber a taboada até a décima: '))
for count in range(10): #para a contagem de 0 até 10 ele segue fazendo o comando abaixo
    print('{}'.format(t*(count+1)))