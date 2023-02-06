#Exercício 7

request = int(input('Digite sua idade em dias: '))
anos = request // 365
meses = (request%365)//30
dias = ((request%365)%12)

print('Você tem {} anos, {} meses e {} dias de idade'.format(anos, meses, dias))