#creo una tupla con cuatro colores
tupla=("rojo","blanco","negro","azul")
entrada= input("Escribe un color:")
entrada= entrada.lower()
#Agrego un lower para que no importe si el usuario pone Rojo o ROJO 
#ya que lo transforma en rojo que es lo que contienen la tupla
if entrada in tupla[0]:
    print('El Rojo es un color admitido.')
elif entrada in tupla[1]:
    print('El Blanco es un color admitido.')
elif entrada in tupla[2]:
    print('El Negro es un color admitido.')
elif entrada in tupla[3]:
    print('El Azul es un color admitido.')
else:
    print("introduciste un calor no admitido")        