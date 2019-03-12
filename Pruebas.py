'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Cliente import *
from Tienda import *

class Pruebas: #Aquí indicamos que la clase Pruebas está vacía, ya que sólo queremos que sea para probar la clase Producto
	pass


#la cantidad de argumentos que se le pasa al constructor, cambia, en este caso son tres
muñeco=Producto("Muñeco Batman","LEGO",650)
triciclo=Producto("Triciclo","Apache",1199)
muñecas=Producto("Set de Muñecas Disney Collection Princesas","DISNEY COLLECTION",2295)
muñeco.imprimirDetalles()
triciclo.imprimirDetalles()
muñecas.imprimirDetalles()

Maria=Cliente("María Pérez",2500)
Margarita=Cliente("Margarita Téllez",1450)
Lucero=Cliente("Lucero Lira",6750)
Maria.imprimirDetalles()
Margarita.imprimirDetalles()
Lucero.imprimirDetalles()

tienda1=Tienda("Play Store",muñeco,Maria)
tienda2=Tienda("Juguetibici",tricilo,Margarita)
tienda3=Tienda("Toy Store",muñecas,Lucero)
tienda1.imprimirDetalles()
tienda2.imprimirDetalles()
tienda3.imprimirDetalles()
