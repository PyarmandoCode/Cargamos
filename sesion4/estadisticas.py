from base_de_datos import empleados
"""
Indicadores
1)Buscar a un empleado por codigo y mostrar el sueldo que gana 
2)Realizar un indicador que me permitar sumar el sueldo de toda
un Area
"""

def buscar_empleado(bd):
    existe=False
    cod_emp=input("Ingrese el codigo del empleado:")
    for item in bd:
        if cod_emp ==  item['codigo']:
            print(f"El Sueldo del empleado {item['nombre']} " 
             + f"{item['apellido']} es {item['sueldo']}")
            existe=True
            break
    if existe == False:
        print("El Empleado no existe")

# def suma_sueldos_area(bd):
#     area=input("Ingrese el Area a totalizar el sueldo:")
#     "sistemas"

#     print("El Total de la planilla del Area {sistemas} es {15800}")        


buscar_empleado(empleados)




