'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Cliente import *

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
  
  def __init__(self,nombre,ubicacion,cliente):
    #Esta ocación, el constructo rebibirá 3 argumentos, donde 2 de ellos son objetos importados de otras clases ya creadas
    self.nombre = nombre
    self.ubicacion = ubicacion
    self.cliente = cliente
  
  def __str__(self): 
    #Este método es para que se visualicen los argumentos de la clase ya creada
    return "El nombre de la tienda es: "+str(self.nombre)+"\nUbicación: "+str(self.ubicacion)+"\n"+str(self.producto)+"\n"+str(self.cliente)
  
  def catalogoProductos:
    #Aquí haremos un método donde 
    print(Los productos disponibles son: ",productos)
