colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#El metodo pop() se usa para eliminar y almacenar el valor eliminado en una variable
Lista=[]
Lista.append(colores.pop(1))
Lista.append(colores.pop(-2))
print("La lista sin el azul y blanco:",colores)
print("La lista nueva con los datos eliminados de la lista anterior",Lista)
