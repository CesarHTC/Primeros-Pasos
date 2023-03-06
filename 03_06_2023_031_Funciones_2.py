#los conocidos como argumentos arbitrarios. Esto nos permite poder pasar
#un número indeterminado de argumentos en las funciones.

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')#Aqui de usa 4 (sin contar el cero como primera posicion)
colores('lila', 'negro', 'rojo')#aqui 3
colores('rosa')#aqui 1
colores('marrón', 'naranja')#aqui 2

#Completa el siguiente fragmento de código:
"""
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores()
"""
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Rojo","Blanco")#El blanco es mi favorito y el rojo no esta mal