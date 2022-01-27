

"""
for .- Cuando se conoce el numero de veces que se repetira el bucle
while.Cuando el bucle termina cuando sucede un valor True
"""
#for num in range(1,10,3):
#    print(num)

# contador=0
# acumulador=0
# for x in range(1,6):
#     sueldo=float(input(f'Ingrese Sueldo {x}:'))
#     contador=contador+1
#     acumulador=acumulador+sueldo
#     promedio_sueldo=acumulador/contador
# print(f'Cantidad de Empleados Procesados {contador}')   
# print(f'El Total de la la Planilla {acumulador}') 
# print(f'El Promedio de Sueldo es {promedio_sueldo}')
# print("Fin del Bucle")    

#Break es salir del Bucle
#Continue es seguir la secuencia del bucle

# for i in range(1,10):
#     if i==7:
#         break
#     else:
#         print(i)
#         continue
        
# i = 0
# suma = 0
# while i<=99:
#     i=i+1
#     suma=suma+i
#     print(i)
# print(f'La Suma de los numeros es {suma}')


#Escribir un programa que nos solicite la contraseña para ingresar al sistema
#Si la contraseña es errada debera volver a intentarlo "n" veces

# contador=0
# contraseña="python"
# usuario=input("Ingrese el Nombre del usuario:")
# while True:
#     con=input("Ingrese la Contraseña:")
#     if con==contraseña:
#         print(f'Bienvenido al Sistema {usuario}')
#         break #True
#     else:
#         contador=contador+1
#         print(f'La Contraseña es errada , vuelva a intentarlo {contador}')
#         if contador == 3:
#             print("Supero los intentos, se bloquera el acceso")
#             break


import random
numero_secreto=random.randint(1,100)
intentos=0
while True:
    numero=int(input("Cual es el numero secreto?"))
    intentos=intentos+1
    if numero==numero_secreto:
        print("Acertastes!!!!!")
        print(f'Numero de Intentos {intentos}')
        break
    else:
        if numero_secreto>numero:
            print(f'El Numero secreto es mayor que {numero}')
        else:
            print(f'El Numero secreto es menor que {numero}')    

#Challenger 1
# Escribir un programa  que solicte ingresar 10 notas de alumnos y nos informe
# cuantos tienes notas mayores  o iguales a 17 y cuantos menores   
# Utilzar while       




    




