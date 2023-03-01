edad = int(input('¿Cuál es tu edad?\n'))
if edad >= 18 and edad <= 45:
	print('Eres un adulto.')
elif edad >= 100 and edad <= 120:
	print('Te vas a morir.')
else:
	print('Eres joven o tienes mas de 120 años.')