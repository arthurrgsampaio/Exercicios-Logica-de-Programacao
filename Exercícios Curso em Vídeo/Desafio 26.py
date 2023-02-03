#Desafio 26
f2 = str(input('Digite qualquer frase para ser analisada: ')).strip()
print("""A letra 'A' aparece: {} vezes
Ela aparece a primeira vez na posição: {}
E a última vez na posição: {}""".format(f2.lower().count('a'), f2.find('a')+1, f2.rfind('a')+1))