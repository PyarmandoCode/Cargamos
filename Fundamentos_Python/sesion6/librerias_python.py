#todo numeros aleatorios
import random
cargamos=['Alicia','Carlos','Javier','Maria','Ana','Nicolle']

# ! Eligiendo un amigo al azar
#print(random.choice(cargamos))
#todo Mostrar un nunero aleatorio
#print(random.randrange(100))


#Trabajando con fechas
import datetime
from datetime import date,datetime
#todo me devuelve la fecha del sistema
hoy = date.today()
#print(hoy)
#todo me devuelve la fecha y hora del sistema
fecha_hora=datetime.now()
#print(fecha_hora)

#todo me devuelve el mes el dia y el año de una fecha establecida
#print(hoy.month)
#print(hoy.day)
#print(hoy.year)

#todo me devuelve la hora , minutos y segundos
#print(f'La Hora Actual: {fecha_hora.hour} ')
#print(f'El Minuto Actual : {fecha_hora.minute} ')
#print(f'Los Segundos: {fecha_hora.second} ')

#todo libreria matematica
import math
# print(math.pi)
# print(math.sqrt(4))
# print(math.cos(math.pi/4))

#todo libreria estadisticas
import statistics
notas=[19,17,20,17,20,14,19,20]

#todo el promedio de notas
print(statistics.mean(notas))
#todo la moda de notas
print(statistics.mode(notas))
#todo el valor medio de los datos
print(statistics.median(notas))





