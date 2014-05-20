memoria = {}
lista_malo = []
lista_bueno = []
memoria['malo'] = lista_malo
memoria['bueno'] = lista_bueno

def RecordBueMal(entrada):
	lista_bueno = memoria['bueno']
	lista_malo = memoria['malo']
	if entrada in lista_malo:
		return False
	elif entrada in lista_bueno:
		return False
	if entrada not in lista_malo:
		return True
	elif entrada not in lista_bueno:
		return True

def AddMem(entrada,buenomalo):
	if RecordBueMal(entrada) == True:
		if buenomalo == 'bueno':
			lista_bueno = memoria['bueno']
			lista_bueno.append(entrada)
		if buenomalo == 'malo':
			lista_malo = memoria['malo']
			lista_malo.append(entrada)

def Reconocer(entrada):
	lista_bueno = memoria['bueno']
	lista_malo = memoria['malo']
	if entrada in lista_malo:
		return entrada + ' es malo.'
	elif entrada in lista_bueno:
		return entrada + ' es bueno.'

while True:
	entrada = raw_input('Introduce algo: ')
	
	RecordBueMal(entrada)
	if RecordBueMal(entrada) == True:
		buenomalo = raw_input('Es "bueno" o "malo"?: ')
	AddMem(entrada,buenomalo)
	if entrada == 'titania':
		print memoria
	print Reconocer(entrada)
