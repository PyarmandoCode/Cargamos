select * from productos;

/* Eliminar los registros de una tabla
reegenerar el indice */
truncate productos;
/* Eliminar la tabla */
drop table productos;

insert into productos(id,nombre_producto,precio,state,picture)
values(1,"Chocolate con Fresa",20,True,'img/chocolate1.jpg');
insert into productos(id,nombre_producto,precio,state,picture)
values(2,"Chocolate con Lucuma",25,True,'img/chocolate2.jpg');
insert into productos(id,nombre_producto,precio,state,picture)
values(3,"Chocolate con Limon",30,True,'img/chocolate3.jpg');
insert into productos(id,nombre_producto,precio,state,picture)
values(4,"Chocolate con Coco",35,True,'img/chocolate4.jpg');
insert into productos(id,nombre_producto,precio,state,picture)
values(5,"Pecana",25,True,'img/chocolate5.jpg');