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
P1=Producto("Muñeco Batman","LEGO",650)
P2=Producto("Triciclo","Apache",1199)
P3=Producto("Set de Muñecas Disney Collection Princesas","DISNEY COLLECTION",2295)
P1.imprimirDetalles()
P2.imprimirDetalles()
P3.imprimirDetalles()

C1=Cliente("Iván Galindo",2500)
C2=Cliente("Margarita Téllez",1450)
C3=Cliente("Lucero Lira",6750)
C1.imprimirDetalles()
C2.imprimirDetalles()
C3.imprimirDetalles()

Tienda1=Tienda("Play Store",P1,C1)
Tienda2=Tienda("Juguetibici",P2,C2)
Tienda3=Tienda("Toy Store",P3,C3)
Tienda1.imprimirDetalles()
Tienda2.imprimirDetalles()
Tienda3.imprimirDetalles()
