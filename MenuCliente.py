from Producto import*
from Cliente import*
from Tienda import*

class MenuCliente:
  def __init__(self):
    pass 

  def registrarCliente(self):
    #Este método es para que el cliente interactue con el MenuCliente y así obtener sus datos
    print("Bienvenido.")
    print("Ingrese su nombre: ")
    nombre = input()
    saldo = input("Ingrese su saldo: ") 
    registro = nombre + saldo

