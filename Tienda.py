'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Cliente import *

class Tienda:
  
  
  def __init__(self,nombre,producto,cliente):
    #Esta ocación, el constructo rebibirá 3 argumentos, donde 2 de ellos son objetos importados de otras clases ya creadas
    self.nombre=nombre
    self.producto=producto
    self.cliente=cliente
  
  def imprimirDetalles(self):
    #Este método es para que se visualicen los argumentos de la clase ya creada
    print("Desde el método:")
    print("El nombre de la tienda es:",self.nombre)
    self.producto.imprimirDetalles
    self.cliente.imprimirDetalles
