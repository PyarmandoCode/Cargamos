class Persona:
    pass

#todo  creando los objetos
#todo instanciando el objeto
pedro = Persona()
cristina=Persona()
manuel=Persona()
maria=Persona()

#print(pedro)
#print(cristina)
#print(manuel)
#print(maria)
class Animal:
    #todo este es un constructor que me permite crear atributos
    def __init__(self,nombre,edad):
        self.nom=nombre
        self.ed=edad
    #todo estos son los metodos o comportamientos de la clase    
    def comer(self):
        if self.ed>10:
            print(f'El Animal {self.nom} debe comer muy poco')
        else:
            print(f'Debes Alimentar mas a {self.nom}')    
            
        
#todo Objetos        
perro=Animal("Pancho",4)
gato=Animal("Paco",11)  
raton=Animal("Topo",8) 

#todo utilizando las metodos
perro.comer()     
gato.comer()
raton.comer()


# print(perro.nom)
# print(perro.ed)
# #todo me permite mostrar todos los atributos del objeto creado
# print(perro.__dict__)
# print(gato.__dict__)
# print(gato.nom)        
    
        

