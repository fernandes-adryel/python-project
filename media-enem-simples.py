print('##Media simples notas do Enem##')

soma=0
cont=1
red=0

print('Redação é por ultimo')

while (cont <=4):
	x = float(input('Digite a nota:' .format(cont)))
	print('proxima nota')
	soma += x
	cont += 1
	if (cont >=5):
   	   red =float( input('Qual é a nota da redação?'.format(red)))
   	   soma=soma + red
media = soma / 5
print('A media é: {}' .format(media))
