'''
March,11
Paula Jorge Hinostrosa
'''

class Cliente:

  #Esta clase recibirá 2 atributos, el nombre del cliente, y el saldo del mismo.
  def __init__(self,nombre,saldo):
    self.nombre=nombre 
    self.saldo=saldo
  
  #Reemplazaremos el método imprimirDetalles por str, que hacen lo mismo, pero el último podría decrise que es más fácil de manejar al ya ser determinado del programa
  def __str__(self):
    return "Nombre del cliente: "+str(self.nombre)+"\nSaldo: $"+str(self.saldo)

