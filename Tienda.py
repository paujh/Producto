'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *

class Tienda:
  
  def __init__(self,nombre,producto):
    self.nombre=nombre
    self.producto=producto
  
  def imprimirDetalles(self):
    #Este método es para que se visualicen los argumentos de la clase ya creada
    print("Desde el método:")
    print("El nombre de la tienda es:",self.nombre)
    self.producto.imprimirDetalles
