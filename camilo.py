def punto3(porcentaje_mesero, porcentaje_impuesto):
	valor_cobrar = int(raw_input("Cual es el total de la venta \n"))
	mesero = (valor_cobrar * porcentaje_mesero) / 100
	print "La propina para el mesero es %d" % (mesero)
	impuesto = (valor_cobrar * porcentaje_impuesto) / 100
	valor_total = valor_cobrar + mesero + impuesto

	print "El valor total a cobrar es %d" % (valor_total)


def punto4(dinero_ingresado):
	impuesto_ganado = (dinero_ingresado * 4) / 100
	valor_regresar = (dinero_ingresado + (impuesto_ganado * 3))

	print valor_regresar

def punto5(millas):
	litros_galon = millas / 0.4
	print litros_galon


def punto3_sec2(numero_lados):
	if numero_lados == 3:
		print "Es un triangulo"

	elif numero_lados == 4:
		print "Cuadrilatero"


def punto1_taller2():
	numeros = []

	while True:
		centinela = int(raw_input("Ingrese numero: "))


		if centinela == 0:
			break

		numeros.append(centinela)

	print numeros
		


def punto4_taller2():
	palabras = []

	while True:
		palabra = raw_input("Ingrese la palabra")

		if palabra == "":
			break
	
		if palabra not in palabras:
			palabras.append(palabra)

	print palabras

#punto3(20, 10)
punto4_taller2()

	
