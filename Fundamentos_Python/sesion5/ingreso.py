"""
todo Para Ingresar a ver el partido entre Perú y Ecuador
todo  se tiene que cumplir los siguientes requisitos
todo que el hincha sea mayor de edad
todo que tenga las 3 dosis de vacuna
todo  si cumple con esas condiciones se le asignara un asiento
todo ojo que no se le puede asignar un asiento repetido
todo al final mostrar los numeros de asientos y personas
todo que lo ocupan
"""
hinchas = [
    {'dni':'10210902','nombre':'Armando','nac':1975,'dosis':3,'asiento':''},
    {'dni':'10210903','nombre':'Diego','nac':2017,'dosis':2,'asiento':''},
    {'dni':'10210904','nombre':'Gilbero','nac':2000,'dosis':1,'asiento':''},
]

resp=""
año_actual=2022
while resp!="N":
    dni=input("Ingresar el DNI:")
    for item in hinchas:
        if (dni in item['dni']):
            edad=año_actual - item['nac']
            if edad>=18 and 3 == item['dosis']:
                asiento=input("Asignar un numero de asiento:")
                item['asiento']=asiento
                print(f'se le asigno el asiento {asiento} al hincha')
            else:
                print("El Hincha no cumple con alguna de las condiciones")
            resp=input("Desea continuar <S/N>:")
            if resp == "N" :break
print(hinchas)

