'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Cliente import *
from Carrito import *

muneco = Producto("Muñeco Batman","LEGO",650)
triciclo = Producto("Triciclo","Apache",1199)
munecas = Producto("Set de Muñecas Disney Collection Princesas","DISNEY COLLECTION",2295)
camacoche = Producto("Cama coche Cilek gris","CILEK",10149)
buz = Producto("Disney Pixar Toy Story Buzz Lightyear","TOY STORY",2649)
elsa = Producto("Muñeca Disney Collection Toddler Elsa","DISNEY COLLECTION",509)
vehiculo = Producto("Vehículo Armable Todoterreno Rextremo de Rex Lego","LEGO",599)
figuras = Producto("Set de figuras Disney Collection Toy Story","DISNEY COLLECTION",339)
casa = Producto("Casa LOL Surprise","L.O.L",7499)
rayo = Producto("Coche a Control Remoto Rayo McQueen Disney Collection","DISNEY COLLECTION",636)

productos = [muneco,triciclo,munecas,camacoche,buz,elsa,vehiculo,figuras,casa,rayo]

class Tienda:
 
  def __init__(self,cliente):
    self.cliente = cliente    
    nombre = "Play Store"
    ubicacion = "Avenida Cuauhtémoc 643, Narvarte Poniente, 03020 Ciudad de México, CDMX"
  
  def __str__(self): 
    #Este método es para que se visualicen los argumentos de la clase ya creada
    return "El nombre de la tienda es: "+str(self.nombre)+"\nUbicación: "+str(self.ubicacion)+"\n"+str(self.producto)+"\n"+str(self.cliente)
  
  def catalogoProductos:
    #Aquí haremos un método donde 
    print("Los productos disponibles son: \n",str(productos))
    eleccion = input("\n¿Desea agregar algún artículo a su carrito? Introduzca su respuesta (SI / NO): ")
    if eleccion == "SI":
      articulo = input("Introduzca el nombre del articulo que desea agregar al carrito: ")
      for i in range (0,len(Tienda.productos)):
				if articulo == Tienda.productos[i].nombre:
					self.cliente.carrito.append(Tienda.productos[i])
					print("Operación exitosa. Ha agregado  el artículo '",articulo,"' a su carrito.")
    else: 
      decision = input("¿Desea comprar los artículos de su carrito? (SI / NO): ")
      if decision == "SI":
        Cliente.comprar
      else: 
        pass
    
    def eliminar(self,producto):
		  self.carrito.eliminarProducto(producto) 
      
    
