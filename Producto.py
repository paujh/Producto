'''
March.03
Paula Jorge Hinostrosa
'''

class Producto:
	
  def __init__(self,nombre,marca,precio):
  #Le damos los atributos que deseemos a la clase, en este caso, tres.
  #Entonces, el constructor recibirá tres argumentos.
    self.nombre=nombre 
    self.marca=marca
    self.precio=precio

  def imprimirDetalles(self):
    #Este método es para que se visualicen los argumentos de la clase ya creada
    print("Desde el método:") 
    print("Nombre del producto:",self.nombre)
    print("Marca:",self.marca)
    print("El precio es: $",self.precio)
