'''
February,03
Paula Jorge Hinostrosa
'''

from Producto import *

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
