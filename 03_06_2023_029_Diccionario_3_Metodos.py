teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
#Elimina el diccionario teclado1 entero . 
#De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola

#Puedes eliminar un diccionario entero con el método del 
#escribiendo del nombre_diccionario 

del teclado1
#solamente eliminar una clave de diccionario de esta forma:
del teclado2['Categoría']
del teclado2['Precio']

print(teclado2['Modelo'])
#si intentamos mostrar la categoria precio nos marca error
#print(teclado2['Precio'])
