from Cliente import*
from Producto import*

class Carrito: 
  #Haremos una clase carrito para meter los productos que el cliente elija
  def __init__(self):
    self.carrito = carrito
      
  def agregarProducto(self,p):
    #Método para agregar un producto al carrito
    carrito.append(p)

  def eliminarProducto(self,r):
    #Método para eliminar un producto del carrito
    carrito.remove(r)

  def __str__(self):
    #Método para desplegar los productos contenidos en el carrito
    "En tu carrito están estos productos: " + str(carrito)
  
  def comprar(self):
    #En este método haremos la suma de los precios de los productos del carrito, y veremos si el cliente puede o no comprar. 
    suma = 0
    n=len(carrito)
    for i in range (n):
      #Profesora, esta parte no estuve segura de como se debía de escribir para sumar los precios de los productos del carrito, por lo mismo, si pudiera corregir el código se lo agradecería mucho.
      suma = math.floor(suma + (carrito.producto.precio[i]))
    return suma 
      #Por lo mismo, ya no supe cómo poner el condicional para ver si el cliente tiene el saldo suficiente
      
    
  
 
