"""
CSV Vamos separados por comas
Es un formato de archivo simple que se utiliza para
Almacenar datos tabulares , como una hoja de calculo o una BD
Es un formato muy comun para Data Sciencie
"""
import csv
#todo esto me permite abrir el archivo en la variable asignada "data_cargamos"
with open('sesion6/cargamos.csv','r') as data_cargamos:
    #!Leer el archivo linea por linea
    csv_leer=csv.reader(data_cargamos)
    #? Convirtiendo o Cast el archivo a un coleccion de tipo List
    lista_estudiantes=list(csv_leer)
    print(lista_estudiantes)
    
    

