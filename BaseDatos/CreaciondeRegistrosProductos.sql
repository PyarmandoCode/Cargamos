use bdcargamos;
show tables;
select * from alumnos;
select * from grupos;
/*Alumnos del GRUPO1 */
select * from alumnos where codgrupo='G1';
select * from alumnos where codgrupo='G3';
select * from alumnos where codgrupo='G4';
select * from alumnos where codgrupo='G5';

select * from productos;

insert into productos(id,nombre_producto,precio,state)
values(1,"Chocolate con Fresa",20,True);
insert into productos(id,nombre_producto,precio,state)
values(2,"Chocolate con Lucuma",25,True);
insert into productos(id,nombre_producto,precio,state)
values(3,"Chocolate con Limon",30,True);
insert into productos(id,nombre_producto,precio,state)
values(4,"Chocolate con Coco",35,True);
