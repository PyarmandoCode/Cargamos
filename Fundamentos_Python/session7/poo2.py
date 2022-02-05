# todo realizar un programa que muestre la informacion
# todo del candidato a evaluar en su nuevo puesto
# todo utilize POO

class Candidato:
    def __init__(self,apellido='Ruiz',nombre='Armando',edad=46,pais='Perú',ciudad='Lima'):
        self.ape=apellido
        self.nom=nombre
        self.ed=edad
        self.pa=pais
        self.ciudad=ciudad
        self.habilidades=[]
        
    def candidato_info(self):
        return f'{self.nom} {self.ape} tiene {self.ed} y es del pais {self.pa} y la ciudad de {self.ciudad} '   
    def adicionar_habilidades(self,habililidad):
        self.habilidades.append(habililidad)

#todo creando el objeto        
candidato3=Candidato("Ramos","Jose",29,"Mexico","DF")
#todo usando el metodo
candidato3.adicionar_habilidades("PYTHON")
candidato3.adicionar_habilidades("FLASK")
candidato3.adicionar_habilidades("DJANGO")
candidato3.adicionar_habilidades("VUE")
print(candidato3.habilidades)
        

# candidato1=Candidato()
# candidato2=Candidato('Gonzales','Pedro',34,'Mexico','DF')
# print(candidato1.candidato_info())
# print(candidato2.candidato_info())


