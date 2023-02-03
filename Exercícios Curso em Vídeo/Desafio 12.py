#Desafio 12
pi = float(input('Insira o valor do produto: ')) #preço antes do desconto
desconto = float(0.95)
pd = pi*desconto #preço após desconto de 5%
print('Após a aplicação do desconto o valor do produto ficou R${:.2f}'.format(pd))