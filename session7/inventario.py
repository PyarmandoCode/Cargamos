# todo crear un programa utilizando Poo que me permita Listar
# todo los productos que estan suspendidos
# todo crear los atributos de acuerdo a los campos del excel
# todo hacer un metodo que nos permita cargar la informacion 
# todo del csv
# todo crear otro metodo que nos liste los productos suspendidos
# todo POO

import csv
class Productos:
    def __init__(self,IdProducto="",NombreProducto="",Proveedor="",Categoría="",CantidadPorUnidad="",PrecioUnidad="",UnidadesEnExistencia="",UnidadesEnPedido="",NivelNuevoPedido="",Suspendido=""):
        self.IdProducto=IdProducto,
        self.NombreProducto=NombreProducto,
        self.Proveedor=Proveedor,
        self.Categoría=Categoría,
        self.CantidadPorUnidad=CantidadPorUnidad,
        self.PrecioUnidad=PrecioUnidad,
        self.UnidadesEnExistencia=UnidadesEnExistencia,
        self.UnidadesEnPedido=UnidadesEnPedido,
        self.NivelNuevoPedido=NivelNuevoPedido,
        self.Suspendido=Suspendido
        self.productos=[]
        
    def cargar_productos(self):
        with open('session7/productos.csv','r') as data_cargamos:
            csv_leer=csv.reader(data_cargamos)
            self.productos=list(csv_leer)
            suspendidos=[]
            for self.IdProducto,self.NombreProducto,self.Proveedor,self.Categoría,self.CantidadPorUnidad,self.PrecioUnidad,self.UnidadesEnExistencia,self.UnidadesEnPedido,self.NivelNuevoPedido,self.Suspendido in self.productos:
                if self.Suspendido=='VERDADERO':
                    suspendidos.append((self.NombreProducto,self.Suspendido))
            return suspendidos    
        
            
data=Productos()
print(data.cargar_productos() ) 