#Desafio 25
ns = str(input('Digite seu nome completo: '))
tem = ns.lower().find('silva')
if tem >= 0:
    print('Você possui Silva em seu nome')
else:
    print('Você não possui silva em seu nome')