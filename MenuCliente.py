import Producto.py
import Cliente.py
import Tienda.py 

class MenuCliente:
  def __init__(self):
    pass 

  def registrarCliente(self):
    #Este método es para que el cliente interactue con el MenuCliente y así obtener sus datos
    print("Ingrese su nombre: ")
    nombre = input()
    saldo = input("Ingrese su saldo: ") 
    registro = nombre + saldo

print("Bienvenido.")
cliente1 = Cliente(nombre,saldo)
print(cliente1)
