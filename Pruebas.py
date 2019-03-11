'''
March,11
Paula Jorge Hinostrosa
'''

from Producto import *
from Tienda import *

class Pruebas: #Aquí indicamos que la clase Pruebas está vacía, ya que sólo queremos que sea para probar la clase Producto
	pass

print ("Imprimimos atributos desde el archivo principal(Producto)")#Indicamos al usuario que la información se tomará desde "Producto"

#la cantidad de argumentos que se le pasa al constructor, cambia, en este caso son tres
P1=Producto("Muñeco Batman","LEGO",650)
P2=Producto("Triciclo","Apache",1199)
P3=Producto("Set de Muñecas Disney Collection Princesas","DISNEY COLLECTION",2295)
P1.imprimirDetalles()
P2.imprimirDetalles()
P3.imprimirDetalles()

Tienda1=Tienda("Play Store",P1)
Tienda2=Tienda("Juguetibici",P2)
Tienda3=Tienda("Toy Store",P3)
Tienda1.imprimirDetalles()
Tienda2.imprimirDetalles()
Tienda3.imprimirDetalles()
