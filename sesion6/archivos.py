"""
CSV Vamos separados por comas
Es un formato de archivo simple que se utiliza para
Almacenar datos tabulares , como una hoja de calculo o una BD
Es un formato muy comun para Data Sciencie
"""
import csv
#todo esto me permite abrir el archivo en la variable asignada "data_cargamos"

def data_alumnos_csv():
    with open('sesion6/cargamos.csv','r') as data_cargamos:
        csv_leer=csv.reader(data_cargamos)
        lista_estudiantes=list(csv_leer)
        return lista_estudiantes
            
def cursos_alumnos(estudiantes,curso_param):
    estudiantes_curso=[]
    for CODIGO,NOMBRE,APELLIDOS,CURSO,P1,P2,P3,PRO in estudiantes:
        if CURSO==curso_param:
            estudiantes_curso.append((NOMBRE,CURSO))
    return estudiantes_curso

#curso=input("Ingrese el curso a mostrar sus estudiantes:")        
#print(cursos_alumnos(data_alumnos_csv(),curso))       


def nota_mayor_curso(estudiantes):
    con=0
    nota_mayor = 0.0
    prom_alum=0
    for cod,nom,ape,cur,p1,p2,p2,pro in estudiantes:
        if con > 0:
            prom_alum = float(pro)
            if float(prom_alum) >= float(nota_mayor):
                #todo intercambio de notas
                nota_mayor = pro  
        con=con+1
    return nota_mayor


print(nota_mayor_curso(data_alumnos_csv()))
#print(nota_mayor_curso(data_alumnos_csv())) 