dvd_precios = [
    {'genero':'SALSA','precio':56.00},
    {'genero':'ROCK','precio':63.00},
    {'genero':'POP','precio':87.00},
    {'genero':'FOLKLORE','precio':120.50},
]


obsequio=False
encontrar=False
genero =input("Ingrese el Genero a comprar:")
for item in dvd_precios:
    if genero in item['genero']:
        encontrar=True
        cant_dvd=int(input("Ingrese la cantidad de DVD a comprar:"))
        #todo estableciendo el descuento
        if cant_dvd>=1 and cant_dvd<=3:
            descuento=0
        elif cant_dvd==4:
            descuento=0.60
        elif cant_dvd>5 and cant_dvd<=10:
            descuento=0.80
        else:
            descuento=10.2
        #todo Para entregar el obsequio    
        if genero.upper()=="POP" or genero.upper()=="ROCK" and cant_dvd>6:
            obsequio=True
        #todo calcular los totales generales
        importe=item['precio']*cant_dvd
        descuento_total=importe*descuento
        importe_pagar=importe-descuento
        print(f'El Total a Pagar {importe_pagar} Tiene Poster {obsequio}')  
if encontrar==False:
    print("El Genero no esta Disponible")    





