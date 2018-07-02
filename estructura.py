class Tipo:
	def __init__(self,clase):
		self.clase = clase
class Castillo:
	def __init__(self,nombre_castillo,nivel,ubicacion):
		"""Recibe una cadena, un size_t, un clase grafo"""
		self.nivel=nivel
		self.nombre=nombre_castillo
		self.puntos_resistencia=nivel*100
		self.ubicacion=ubicacion
	def ver_aldea_adyacentes(self):
		"""Revuelve una lista con las aldeas"""
		lista_aux = []
		vertice_ady = self.ubicacion.adyacentes_vertice()
		for vertice in vertice_ady:
			if vertice.tipo=="ALDEA":
				lista_aux.append(vertice)
		return vertice_ady
class Aldea:
	def __init__(self,nombre_aldea,cantidad_de_habitante,nivel,impuesto):
		self.nombre = nombre_aldea
		self.impuesto = impuesto
		self.felicidad = 100-impuesto
		self.poblacion = cantidad_de_habitante
		self.nivel = nivel
	def cobrar_impuesto(self):
		return self.poblacion*self.impuesto

		

