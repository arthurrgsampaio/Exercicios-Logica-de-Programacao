#Desafio 11
ap = float(input('Digite a altura da parede em metros: '))
lp = float(input('Digite a largura da parede em metros: '))
rendimento = (ap*lp)/2

print('Serão necessários {:.2f}L de tinta para pintar a parede'.format(rendimento))