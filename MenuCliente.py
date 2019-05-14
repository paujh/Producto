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
    cliente = Tienda(Cliente(nombre,saldo))
    cliente.almacenagregar()
		while 0<1:
			eleccion=input("\n¿Que desea hacer?:\na)Ver carrito\nb)Comprar\nc)Eliminar producto del carrito\nEscriba su elección 'a', 'b' o 'c': ")
			if eleccion == "a":
				cliente.almacenagregar()
			elif eleccion == "b":
				cliente.comprar()
			elif eleccion == "c":
				Eliminarproducto = input("\nIntroduzca el nombre del articulo que desea eliminar: ")
				cliente.eliminar(Eliminarproducto)
  

