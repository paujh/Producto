'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Cliente import *
from Carrito import *
import csv

class Tienda:
 
  def __init__(self,cliente):
    self.cliente = cliente    
    nombre = "Play Store"
    ubicacion = "Avenida Cuauhtémoc 643, Narvarte Poniente, 03020 Ciudad de México, CDMX"
  
  def __str__(self): 
    #Este método es para que se visualicen los argumentos de la clase ya creada
    return "El nombre de la tienda es: "+str(self.nombre)+"\nUbicación: "+str(self.ubicacion)

  def catalogoProductos:
    #Aquí haremos un método donde se muestran los productos de la tienda
    csvarchivo = open('productos.csv')
    entrada = csv.reader(csvarchivo)
    print("Los productos disponibles son:\n")
    for reg in entrada:
      nombre, marca, precio = next(entrada)
      print(nombre, marca, precio)
    eleccion = input("\n¿Desea agregar algún artículo a su carrito? Introduzca su respuesta (SI / NO): ")
    if eleccion == "SI":
      articulo = input("Introduzca el nombre del articulo que desea agregar al carrito: ")
      for i in range (0,len(reg)):
	if articulo == nombre:
	   self.cliente.carrito.append(nombre, marca, precio)
	   print("Operación exitosa. Ha agregado  el artículo '",articulo,"' a su carrito.")
    else: 
      decision = input("¿Desea comprar los artículos de su carrito? (SI / NO): ")
      if decision == "SI":
        Cliente.comprar
      else: 
        pass
    
    def eliminar(self,producto):
		  self.carrito.eliminarProducto(producto) 

csvarchivo.close() 
