class Peliculas:
    def __init__(self,nombre,duracion,idioma,año):
        self.nombre=nombre
        self.duracion=duracion
        self.idioma=idioma
        self.año=año
    #todo el metodo Str(STRING) nos permite visualizar su contenido cuando se 
    #todo llama al objeto    
    def __str__(self):
        return f'{self.nombre}'
    def IniciarPelicula(self,play):
        if play == True:
            print(f'La Pelicula {self.nombre}  ha Iniciado')
        else:
            print("La Pelicula no se ha Iniciado")   
    def PausarPelicula(self,pausa):
        if pausa == True:
            print(f'La Pelicula {self.nombre}  se ha pausado')
        else:
            print("La Pelicula prosigue")      
            
#todo Herencia entre clase Hija - Padre Peliculas
class Comedia(Peliculas):
    def __init__(self, nombre, duracion, idioma, año,pais):
        super().__init__(nombre, duracion, idioma, año)
        self.pais=pais
    def agregarsubtitulos(self,sub):
        if sub==True:
            print(f'La pelicula {self.nombre} tiene subtitulos')
        else:
            print(f'La pelicula {self.nombre} NO tiene subtitulos')   
                
    
pelicula2=Comedia("Scary Movie","90 min","Ingles","2000","USA")   
print(pelicula2.__dict__)     
pelicula2.agregarsubtitulos(True)
        

#pelicula1=Peliculas("Scary Movie","90 min","Ingles","2000") 
#pelicula1.IniciarPelicula(False)
#pelicula1.PausarPelicula(False)
#print(pelicula1)
#print(pelicula1.__dict__)       