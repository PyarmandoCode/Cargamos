
try:
    # todo el cuerpo de programa
    suma = 20 + "15"
    print(suma)
    # todo la palabra reservada excepcion nos devuelve el error del interprete
except Exception as error:
    # ! cuando el programa encuentre un error entrara a este bloque
    print(f'Ha ocurrido un excepcion {error}' )
else:
    # ? Cunado no ocurra ningun error
    print("No Ha Existido ninguna excepcion")
finally:
    # todo siempre se va a ejecutar
    print("Se termino el bloque de codigo")            
    
    
#suma = 20 + "15"
#print(suma)    