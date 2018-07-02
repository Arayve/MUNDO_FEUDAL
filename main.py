import csv
ARCHIVO_DATA= "memoria.txt"

def nueva_partida(nombre_partida,nombre_archivo):
	with open(ARCHIVO_DATA,"a") as archivo:
		archivo.write("{},{}\n".format(nombre_partida,nombre_archivo))
nueva_partida("XCRISWMES","archivo1.txt")


