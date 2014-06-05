memoria = {}
lista_malo = []
lista_neutro = []
lista_bueno = []
memoria['malo'] = lista_malo
memoria['neutro'] = lista_neutro
memoria['bueno'] = lista_bueno

def RecordBueMal(entrada):
	lista_bueno = memoria['bueno']
	lista_neutro = memoria['neutro']
	lista_malo = memoria['malo']
	if entrada in lista_malo:
		return False
	else:
		return True
	if entrada in lista_neutro:
		return False
	else:
		return True
	if entrada in lista_bueno:
		return False
	else:
		return True

def AddMem(entrada,buenomalo):
	if RecordBueMal(entrada) == True:
		if buenomalo == 'bueno':
			lista_bueno = memoria['bueno']
			lista_bueno.append(entrada)
		if buenomalo == 'neutro':
			lista_neutro = memoria['neutro']
			lista_neutro.append(entrada)
		if buenomalo == 'malo':
			lista_malo = memoria['malo']
			lista_malo.append(entrada)

def Reconocer(entrada):
	lista_bueno = memoria['bueno']
	lista_neutro = memoria['neutro']
	lista_malo = memoria['malo']
	if entrada in lista_malo:
		return entrada + ' es malo.'
	elif entrada in lista_neutro:
		return entrada + ' es neutro'
	elif entrada in lista_bueno:
		return entrada + ' es bueno.'

print '''
Opciones:
show_memory => Ver memoria.
push_file => Exportar memoria en archivo.
push_memory => Importar archivo a memoria.

'''

while True:
	entrada = raw_input('Introduce algo: ')
	
	RecordBueMal(entrada)
	if RecordBueMal(entrada) == True and entrada != 'show_memory' and entrada != 'push_file' and entrada != 'push_memory':
		buenomalo = raw_input('Es "bueno", "neutro", "malo"?: ')
		AddMem(entrada,buenomalo)
	if entrada == 'show_memory':
		print memoria
	elif entrada == 'push_file':
		fil = open('memory.cr','w')
		memfil = 'memoria = ' + str(memoria)
		fil.write(memfil)
		fil.close()
	elif entrada == 'push_memory':
		fil = open('memory.cr','rw')
		memfil = ''
		for lin in fil:
			memfil = memfil + lin
			memfil = memfil.replace("\n","")
		fil.close()
		exec memfil
	print Reconocer(entrada)
