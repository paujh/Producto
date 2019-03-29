'''
March.03
Paula Jorge Hinostrosa
'''

class Producto:
	
  def __init__(self,nombre,marca,precio):
  #Le damos los atributos que deseemos a la clase, en este caso, tres.
  #Entonces, el constructor recibirá tres argumentos.
    self.nombre = nombre 
    self.marca = marca
    self.precio = precio

  def __str__(self):
    #Este método lo usaremos para reemplazar "imprimirDetalles".
    #Ejecutará la misma función, que es mostrar al usuario la información del objeto que se proporcione respecto a la clase	
    return "Nombre del producto:"+str(self.nombre)+"\nMarca:"+str(self.marca)+"\nPrecio: $"+str(self.precio)

