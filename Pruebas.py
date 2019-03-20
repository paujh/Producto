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
print(str(muñeco)
print(str(triciclo)
print(str(muñecas)

maria=Cliente("María Pérez",2500)
margarita=Cliente("Margarita Téllez",1450)
lucero=Cliente("Lucero Lira",6750)
print(str(maria)
print(str(margarita)
print(str(lucero)
      
tienda1=Tienda("Play Store","Avenida Cuauhtémoc 643, Narvarte Poniente, 03020 Ciudad de México, CDMX",muñeco,Maria)
tienda2=Tienda("Juguetibici","Casi Esq. con Jose Zubieta., Calle Ignacio Zaragoza, Juan Escutia, 09100 Ciudad de México, CDMX",tricilo,Margarita)
tienda3=Tienda("Toy Store","Parroquia 179, Col del Valle Sur, 03100 Ciudad de México, CDMX",muñecas,Lucero)
print(str(tienda1)
print(str(tienda2)
print(str(tienda3)
