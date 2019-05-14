from Cliente import*
from Producto import*

class Carrito: 
  #Haremos una clase carrito para meter los productos que el cliente elija
  def __init__(self):
    self.carrito = carrito
      
  def agregarProducto(self,p):
    #Método para agregar un producto al carrito
    self.carrito.append(p)

  def eliminarProducto(self,r):
    #Método para eliminar un producto del carrito
    self.carrito.remove(r)

  def __str__(self):
    #Método para desplegar los productos contenidos en el carrito
    "En tu carrito están estos productos: " + str(carrito)
  
 def comprar(self): #permite realizar compras (de manera primitiva)
		Total = 0
		for i in range(0,len(self.carrito)):
			Total = Total + self.carrito[i].precio
		return Total
    if Total > Cliente.saldo:
      print("No tienes saldo suficiente")
    else:
      print("Compra realizada")
      
      
    
  
 
