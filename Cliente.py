'''
March,11
Paula Jorge Hinostrosa
'''

class Cliente:

  #Esta clase recibirá 2 atributos, el nombre del cliente, y el saldo del mismo.
  def __init__(self,nombre,saldo):
    self.nombre = nombre 
    self.saldo = saldo
    self.carro = []
  
  #Reemplazaremos el método imprimirDetalles por str, que hacen lo mismo, pero el último podría decrise que es más fácil de manejar al ya ser determinado del programa
  def __str__(self):
    return "Nombre del cliente: "+str(self.nombre)+"\nSaldo: $"+str(self.saldo)
  
  def agregarCarrito(self,producto): #Agrega un productos seleccionados por el usuario al carrito del cliente.
		carro1 = Carrito()
		carro1.agregar(producto)
		self.carro = carro1.carrito
    
  def comprar(self): #Permite realizar la compra de los productos del carrito, si es que el cliente cuenta con saldo suficiente.
		Total = 0
		for i in range(0,len(self.carro)):
			Total = Total + self.carro[i].precio
		if float(Total) > float(self.saldo):
			print("\n No tienes saldo suficiente para realizar tu compra")
		else:
			self.saldo = float(self.saldo) - float(Total)
			print("Tu compra ha sido realizada.")
