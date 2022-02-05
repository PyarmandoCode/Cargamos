precios = (100,200,300)
valores=1,2,3,4,5,6,7

#print(type(precios))
#print(type(valores))
#todo las tuplas son inmutables no se pueden modificar
#todo ni insertar ni eliminar
#todo son ordenados
#print(precios)
#precios[0]=200
#print(precios[0])
#print(len(precios))

frutas=("manzanass","fresas","uvas")
buscar=input("Ingresa la fruta a buscar:")
if buscar in frutas:
    print("Si se encuentra la fruta")
else:
    print("No se encuenta la fruta")    
