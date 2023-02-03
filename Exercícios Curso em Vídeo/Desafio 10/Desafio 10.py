#Desafio 10
carteira = float(input('Digite quantos reais você possui: '))
dolar = float(3.27)
doleal = carteira/dolar
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(carteira, doleal))