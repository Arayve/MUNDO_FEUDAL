"""Clase castillo"""
class Castillo:
	def __init__(self,nombre_castillo,nivel,ubicacion):
		self.nivel=nivel
		self.nombre=nombre_castillo
		self.puntos_resistencia=nivel*100
		self.ubicacion=ubicacion
"""Clase aldea"""
class Aldea:
	def __init__(self,nombre_aldea,cantidad_de_habitante,nivel):
		self.nombre=nombre_aldea
		self.poblacion=cantidad_de_habitante
		self.nivel=nivel
	def cobrar_impuesto(self):
		return self.poblacion*self.nivel
		

